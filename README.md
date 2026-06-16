# nike-counterfeit-shoe-yolov12
Real-time counterfeit Nike shoe detection using YOLOv12 object detection with bounding box classification.
# 👟 Counterfeit Nike Shoe Detection — YOLOv12

A deep learning-based computer vision project that detects and classifies 
Nike shoes as **authentic** or **counterfeit** in real time using YOLOv12.

## 🔍 Overview
Counterfeit footwear is a growing problem in the fashion industry. 
This project leverages YOLOv12 object detection to automatically identify 
visual differences between genuine and fake Nike shoes from images or live webcam feed.

## 📦 Dataset
- Source: Kaggle — `aureliofoni/nikeshoes-counterfeit`
- 7,723 labeled images
- Split into train / validation / test sets
- YOLO-format bounding box annotations

## 🧠 Model
- Architecture: YOLOv12 (Ultralytics)
- Task: Object Detection & Classification
- Classes: `real`, `fake`
- Training: Google Colab (T4 GPU)

## 🚀 Features
- Real-time webcam detection with bounding boxes
- Upload custom images for instant authentication
- Confidence score displayed per detection

## 🛠️ Tech Stack
- Python
- YOLOv12 (Ultralytics)
- OpenCV
- Google Colab
- Kaggle
