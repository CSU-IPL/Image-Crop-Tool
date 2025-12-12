"""
Interactive Image Cropping Tool
Author: Goodman
Description: An interactive tool for selecting and cropping regions from images.
             Supports both square and free-form rectangle selection modes.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class ImageCropper:
    """
    Interactive image cropping tool with mouse and keyboard controls.
    
    Features:
        - Draw rectangular selection with left mouse button
        - Move selection with right mouse button
        - Toggle between square and free-form modes
        - Real-time preview of selection
        - Output coordinates for batch processing
    
    Controls:
        Left Click & Drag: Draw rectangular selection
        Right Click & Drag: Move existing selection
        Key 'A': Toggle square/free-form mode
        Key 'C': Crop and save selected area
        Key 'R': Reset selection
        Key 'Q': Quit program
    """
    
    def __init__(self, image_path):
        """
        Initialize the ImageCropper with an image.
        
        Args:
            image_path (str): Path to the image file
            
        Raises:
            ValueError: If image cannot be loaded
        """
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Cannot load image, please check the path")
        
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 转换为RGB格式
        self.original_image = self.image.copy()
        
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        # 可配置的线宽（像素）
        self.linewidth = 2
        # 可配置的边框颜色
        self.edgecolor = '#FF0000'
        self.rect = None
        self.ix, self.iy = -1, -1
        self.fx, self.fy = -1, -1
        self.square_mode = True
        self.drawing = False
        self.moving = False
        self.move_start_x, self.move_start_y = -1, -1
        self.width, self.height = 0, 0
        
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        
        plt.title("Left click: Draw, Right click: Move, C: Crop, R: Reset, A: Square/Free, Q: Quit")
        plt.show()

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
            
        # 左键绘制矩形
        if event.button == 1:  # 鼠标左键
            # 如果已经有一个矩形且不在绘制中，先清除它
            if self.rect is not None and not self.drawing and not self.moving:
                self.rect.remove()
                self.fig.canvas.draw()
                
            self.drawing = True
            self.moving = False
            self.ix, self.iy = int(event.xdata), int(event.ydata)
            self.fx, self.fy = self.ix, self.iy
            self.rect = Rectangle((self.ix, self.iy), 0, 0, linewidth=self.linewidth, edgecolor=self.edgecolor, facecolor='none')
            self.ax.add_patch(self.rect)
            self.fig.canvas.draw()
            
        # 右键移动矩形
        elif event.button == 3:  # 鼠标右键
            if self.rect is not None and not self.drawing:
                self.drawing = False
                self.moving = True
                self.move_start_x, self.move_start_y = int(event.xdata), int(event.ydata)
                self.width = self.fx - self.ix
                self.height = self.fy - self.iy

    def on_motion(self, event):
        if event.inaxes != self.ax:
            return
            
        # 绘制矩形
        if self.drawing and self.rect is not None:
            self.fx, self.fy = int(event.xdata), int(event.ydata)
            
            if self.square_mode:
                side = max(abs(self.fx - self.ix), abs(self.fy - self.iy))
                self.fx = self.ix + side if self.fx > self.ix else self.ix - side
                self.fy = self.iy + side if self.fy > self.iy else self.iy - side
            
            width = self.fx - self.ix
            height = self.fy - self.iy
            
            self.rect.set_width(width)
            self.rect.set_height(height)
            self.fig.canvas.draw()
            
        # 移动矩形
        elif self.moving and self.rect is not None:
            move_current_x, move_current_y = int(event.xdata), int(event.ydata)
            dx = move_current_x - self.move_start_x
            dy = move_current_y - self.move_start_y
            
            # 更新矩形的位置
            self.ix = self.ix + dx
            self.iy = self.iy + dy
            self.fx = self.ix + self.width
            self.fy = self.iy + self.height
            
            # 更新起始移动点
            self.move_start_x, self.move_start_y = move_current_x, move_current_y
            
            # 重绘矩形
            self.rect.remove()
            self.rect = Rectangle((self.ix, self.iy), self.width, self.height, 
                                linewidth=self.linewidth, edgecolor=self.edgecolor, facecolor='none')
            self.ax.add_patch(self.rect)
            self.fig.canvas.draw()

    def on_release(self, event):
        if self.drawing:
            self.drawing = False
            # 计算宽度和高度
            self.width = self.fx - self.ix
            self.height = self.fy - self.iy
            
            # 获取左上角坐标和矩形尺寸
            x = min(self.ix, self.fx)
            y = min(self.iy, self.fy)
            width = abs(self.width)
            height = abs(self.height)
            
            # 简洁输出：左上角坐标 + 宽高
            print(f"Rectangle: x={x}, y={y}, width={width}, height={height}")
        
        elif self.moving:
            self.moving = False
            # 获取左上角坐标和矩形尺寸
            x = min(self.ix, self.fx)
            y = min(self.iy, self.fy)
            width = abs(self.fx - self.ix)
            height = abs(self.fy - self.iy)
            
            # 简洁输出：左上角坐标 + 宽高
            print(f"Moved rectangle: x={x}, y={y}, width={width}, height={height}")

    def on_key(self, event):
        if event.key == 'r':  # 重置
            self.ax.clear()
            self.ax.imshow(self.original_image)
            self.rect = None
            self.ix, self.iy = -1, -1
            self.fx, self.fy = -1, -1
            self.drawing = False
            self.moving = False
            plt.title("Left click: Draw, Right click: Move, C: Crop, R: Reset, A: Square/Free, Q: Quit")
            self.fig.canvas.draw()
            
        elif event.key == 'a':  # 切换方形/自由模式
            self.square_mode = not self.square_mode
            status = "Square" if self.square_mode else "Free"
            plt.title(f"Mode: {status} - Left click: Draw, Right click: Move, C: Crop, R: Reset, A: Square/Free, Q: Quit")
            self.fig.canvas.draw()
            
        elif event.key == 'c':  # 确认剪裁
            if self.ix != -1 and self.iy != -1 and self.fx != -1 and self.fy != -1:
                x = min(self.ix, self.fx)
                y = min(self.iy, self.fy)
                width = abs(self.fx - self.ix)
                height = abs(self.fy - self.iy)
                
                # 简洁输出剪裁坐标：左上角 + 宽高
                print(f"Cropping: x={x}, y={y}, width={width}, height={height}")
                
                cropped = self.original_image[y:y+height, x:x+width]
                plt.close()
                
                # 显示剪裁结果
                plt.figure()
                plt.imshow(cropped)
                plt.title("Cropped Result")
                plt.show()
                
                # 保存剪裁结果
                output_path = "cropped_" + image_path.split('/')[-1]
                cv2.imwrite(output_path, cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
                print(f"Cropped image saved as: {output_path}")
                
        elif event.key == 'q':  # 退出
            plt.close()

if __name__ == "__main__":
    image_path = "images_with_rect\kodim18_0.1958bpp_with_rect.png"
    
    try:
        cropper = ImageCropper(image_path)
    except Exception as e:
        print(f"Error: {e}")