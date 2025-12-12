<div align="center">

# 🖼️ 图像裁剪工具

**一个功能强大的 Python 图像批量裁剪工具**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](README.md) | 简体中文

</div>

---

## 📖 项目介绍

这是一个基于 Python 的图像裁剪和处理工具，提供了交互式界面和批处理功能，可以方便地对图像进行选择、裁剪和分析。该工具主要用于图像处理研究，特别适合需要对多张图像进行相同区域裁剪的场景。

## ✨ 主要功能

### 🎯 1. 交互式图像裁剪 (`plot_rec.py`)

| 功能 | 说明 |
|------|------|
| 🔲 **矩形选择** | 支持自由矩形和正方形两种选择模式 |
| 🖱️ **移动选区** | 使用鼠标右键移动已绘制的选区 |
| 👁️ **实时预览** | 绘制过程中实时显示选区 |
| 📍 **坐标输出** | 自动输出四个角点坐标，方便批处理 |
| ✂️ **裁剪保存** | 一键裁剪并保存选定区域 |

### 📦 2. 批量图像处理 (`crop.py`)

| 功能 | 说明 |
|------|------|
| 🚀 **批量裁剪** | 使用相同坐标对多张图像批量裁剪 |
| 🔴 **矩形标记** | 在原图上绘制红色矩形框标记区域 |
| 💾 **自动保存** | 裁剪结果和标记图像分别保存 |
| 🎨 **多格式支持** | PNG、JPG、JPEG、BMP、TIFF 等 |

##  安装依赖

```bash
pip install opencv-python numpy matplotlib
```

## 🚀 使用方法

### 📍 第一步：交互式获取裁剪坐标

运行 `plot_rec.py` 来交互式地选择你想要裁剪的区域。

```bash
python plot_rec.py
```

**⌨️ 操作说明：**

| 操作 | 功能 |
|------|------|
| 🖱️ **左键拖动** | 绘制矩形选区 |
| 🖱️ **右键拖动** | 移动已绘制的选区 |
| ⌨️ **按键 `A`** | 切换正方形/自由矩形模式 |
| ⌨️ **按键 `C`** | 裁剪并保存，输出坐标 |
| ⌨️ **按键 `R`** | 重置选区 |
| ⌨️ **按键 `Q`** | 退出程序 |

程序运行后，当你确定好选区并松开鼠标（或按下 `C` 键裁剪）时，控制台会输出类似以下的坐标信息：
```
Rectangle: x=239, y=152, width=94, height=94
```
**坐标说明：**
- `x`, `y`: 矩形左上角的坐标
- `width`: 矩形的宽度（像素）
- `height`: 矩形的高度（像素）

请复制这组坐标信息。

### 🔄 第二步：批量处理图像

打开 `crop.py` 文件，找到底部的 `if __name__ == "__main__":` 部分，修改配置：

```python
# 输入文件夹路径
input_folder = "input_images"

# 输出文件夹路径
output_crop_folder = "cropped_images"
output_rect_folder = "images_with_rect"

# 将第一步中获取的坐标填入此处
# 格式：(x, y, width, height)
# x, y: 左上角坐标
# width, height: 矩形的宽度和高度
crop_rect = (239, 152, 94, 94)
```

然后运行脚本：

```bash
python crop.py
```

程序将自动处理 `input_images` 文件夹下的所有图片，生成的裁剪图片保存在 `cropped_images`，带标记的原图保存在 `images_with_rect`。

## 📁 文件结构

```
📦 Crop/
├── 📜 crop.py                    # 批量图像处理脚本
├── 📜 plot_rec.py                # 交互式裁剪与坐标获取工具
├── 📜 README.md                  # 英文说明文档
├── 📜 README_CN.md               # 中文说明文档
├── 📂 input_images/              # [输入] 存放原始图像
├── 📂 cropped_images/            # [输出] 存放裁剪后的图像
└── 📂 images_with_rect/          # [输出] 存放带红色矩形框的图像
```

## ⚠️ 注意事项

- ✅ 确保输入图像路径正确
- ✅ 裁剪坐标应在图像范围内
- ✅ PNG 图像会保留 Alpha 通道

---

<div align="center">
⭐ 如果这个项目对你有帮助，请给个 Star！

</div>

