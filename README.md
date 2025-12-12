<div align="center">

# 🖼️ Image Cropping Tool

**A Powerful Python Batch Image Cropping Tool**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

English | [Chinese](README_CN.md)

</div>

---

## 📖 Introduction

This is a Python-based image cropping and processing tool that provides both an interactive interface and batch processing capabilities. It allows for easy selection, cropping, and analysis of images. This tool is primarily designed for image processing research, especially for scenarios where multiple images need to be cropped using the same region of interest.

## ✨ Features

### 🎯 1. Interactive Image Cropping (`plot_rec.py`)

| Feature | Description |
|---------|-------------|
| 🔲 **Rectangle Selection** | Supports both free-form and square selection modes |
| 🖱️ **Move Selection** | Right-click and drag to move the drawn selection |
| 👁️ **Real-time Preview** | Displays selection in real-time during drawing |
| 📍 **Coordinate Output** | Automatically outputs four corner coordinates for batch processing |
| ✂️ **Crop & Save** | One-key cropping and saving of selected area |

### 📦 2. Batch Image Processing (`crop.py`)

| Feature | Description |
|---------|-------------|
| 🚀 **Batch Cropping** | Crops multiple images using the same coordinates |
| 🔴 **Rectangle Marking** | Draws a red rectangle on original images to mark the area |
| 💾 **Auto Save** | Saves cropped results and marked images separately |
| 🎨 **Multi-format Support** | PNG, JPG, JPEG, BMP, TIFF, etc. |

##  Installation

```bash
pip install opencv-python numpy matplotlib
```

## 🚀 Usage

### 📍 Step 1: Interactively Get Crop Coordinates

Run `plot_rec.py` to interactively select the region you want to crop.

```bash
python plot_rec.py
```

**⌨️ Controls:**

| Operation | Function |
|-----------|----------|
| 🖱️ **Left Click & Drag** | Draw a rectangular selection |
| 🖱️ **Right Click & Drag** | Move the existing selection |
| ⌨️ **Key `A`** | Toggle between Square and Free mode |
| ⌨️ **Key `C`** | Crop, save and output coordinates |
| ⌨️ **Key `R`** | Reset the selection |
| ⌨️ **Key `Q`** | Quit the program |

After selecting the area and releasing the mouse (or pressing `C`), the console will output coordinates like this:
```
Rectangle: x=239, y=152, width=94, height=94
```
**Coordinate explanation:**
- `x`, `y`: Top-left corner coordinates of the rectangle
- `width`: Width of the rectangle (in pixels)
- `height`: Height of the rectangle (in pixels)

Please copy these coordinate values.

### 🔄 Step 2: Batch Process Images

Open `crop.py` and modify the configuration in the `if __name__ == "__main__":` section at the bottom:

```python
# Input folder path
input_folder = "input_images"

# Output folder paths
output_crop_folder = "cropped_images"
output_rect_folder = "images_with_rect"

# Paste the coordinates obtained from Step 1 here
# Format: (x, y, width, height)
# x, y: Top-left corner coordinates
# width, height: Rectangle dimensions
crop_rect = (239, 152, 94, 94)
```

Then run the script:

```bash
python crop.py
```

The program will automatically process all images in the `input_images` folder. Cropped images will be saved in `cropped_images`, and images with the red rectangle mark will be saved in `images_with_rect`.

## 📁 File Structure

```
📦 Crop/
├── 📜 crop.py                    # Batch image processing script
├── 📜 plot_rec.py                # Interactive cropping & coordinate extraction tool
├── 📜 README.md                  # English documentation
├── 📜 README_CN.md               # Chinese documentation
├── 📂 input_images/              # [Input] Folder for original images
├── 📂 cropped_images/            # [Output] Folder for cropped images
└── 📂 images_with_rect/          # [Output] Folder for images with red rectangle marks
```

## ⚠️ Notes

- ✅ Ensure the input image paths are correct
- ✅ Crop coordinates must be within the image boundaries
- ✅ PNG images preserve the Alpha channel

---

<div align="center">
⭐ Star this project if it helps you!


</div>
