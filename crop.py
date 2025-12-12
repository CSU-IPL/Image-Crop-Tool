"""
Batch Image Cropping Tool
Author: Goodman
Description: Batch process multiple images using the same cropping region.
             Creates cropped images and marked originals with rectangle overlay.
"""

import cv2
import numpy as np
import os


def process_images(input_folder, output_crop_folder, output_rect_folder, crop_rect):
    """
    批量处理文件夹中的图片，裁剪相同区域并保存结果
    
    该函数会遍历输入文件夹中的所有图片，使用相同的裁剪区域进行批量处理。
    处理结果包括：
    1. 裁剪后的图片（保存到 output_crop_folder）
    2. 带红色矩形框标记的原图（保存到 output_rect_folder）
    
    Args:
        input_folder (str): 输入图片文件夹路径
        output_crop_folder (str): 裁剪后图片保存文件夹
        output_rect_folder (str): 带矩形框图片保存文件夹
        crop_rect (tuple): 裁剪区域，格式为 (x, y, width, height)
                          x, y: 左上角坐标
                          width, height: 矩形的宽度和高度
    
    Returns:
        None
        
    Example:
        process_images("input_images", "cropped_images", "images_with_rect", (100, 100, 200, 200))
    """
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_crop_folder, exist_ok=True)
    os.makedirs(output_rect_folder, exist_ok=True)
    
    # 解析裁剪区域
    x, y, width, height = crop_rect
    
    # 计算四个角点（用于绘制矩形框）
    pts = np.array([
        [x, y],
        [x + width, y],
        [x + width, y + height],
        [x, y + height]
    ], dtype=np.int32)
    
    # 遍历输入文件夹中的所有图片文件
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')
    processed_count = 0
    
    for filename in os.listdir(input_folder):
        # 检查文件是否为支持的图片格式
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            
            # 读取图片（包括Alpha通道，如果是PNG）
            image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
            if image is None:
                print(f"无法读取图片: {filename}")
                continue
            
            # 1. 剪裁区域
            # 直接使用提供的坐标和尺寸进行裁剪
            cropped = image[y:y+height, x:x+width].copy()
            
            # 2. 在原图上绘制红色矩形框
            if len(image.shape) == 3 and image.shape[2] == 4:  # 如果有Alpha通道
                image_with_rect = image.copy()
                cv2.polylines(image_with_rect[:, :, :3], [pts], isClosed=True, color=(0, 0, 255), thickness=2)
            else:
                image_with_rect = image.copy()
                cv2.polylines(image_with_rect, [pts], isClosed=True, color=(0, 0, 255), thickness=2)
            
            # 生成输出文件名（保留原文件名，添加后缀）
            base_name, ext = os.path.splitext(filename)
            crop_output = os.path.join(output_crop_folder, f"{base_name}_cropped.png")
            rect_output = os.path.join(output_rect_folder, f"{base_name}_with_rect.png")
            
            # 保存结果为PNG格式
            cv2.imwrite(crop_output, cropped, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            cv2.imwrite(rect_output, image_with_rect, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            
            processed_count += 1
            print(f"✓ 处理完成: {filename}")
    
    print(f"\n处理完成！共处理 {processed_count} 张图片")
    print(f"裁剪图片保存在: {output_crop_folder}")
    print(f"标记图片保存在: {output_rect_folder}")


if __name__ == "__main__":
    # 输入文件夹路径
    input_folder = "input_images"  # 替换为你的输入文件夹路径
    
    # 输出文件夹路径
    output_crop_folder = "cropped_images"  # 裁剪图片保存文件夹
    output_rect_folder = "images_with_rect"  # 带矩形框图片保存文件夹
    
    # 裁剪区域：(x, y, width, height)
    # x, y: 左上角坐标
    # width, height: 矩形的宽度和高度
    # 示例：从坐标 (239, 152) 开始，宽度 94，高度 94
    crop_rect = (239, 152, 94, 94)  # 替换为你需要的值
    
    # 处理所有图片
    process_images(input_folder, output_crop_folder, output_rect_folder, crop_rect)