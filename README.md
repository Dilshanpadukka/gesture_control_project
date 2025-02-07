# Gesture Control and Facial Expression Detection System

Interactive system combining gesture-controlled drag-and-drop and facial expression detection.

## Features
- Menu system for switching between modes
- Gesture-controlled drag and drop
- Real-time facial expression detection
- Emotions detected: Happy, Sad, Angry, Neutral, Surprised
- Visual feedback for detected emotions

## Prerequisites
- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Tensorflow
- Keras

## Installation
```bash
pip install -r requirements.txt
```

## Project Structure
```
gesture_face_detection/
│
├── src/
│   ├── __init__.py
│   ├── hand_tracker.py
│   ├── virtual_object.py
│   ├── gesture_detector.py
│   ├── face_detector.py
│   ├── emotion_classifier.py
│   └── utils.py
│
├── models/
│   └── emotion_model.h5
│
├── assets/
│   └── objects.json
│
├── requirements.txt
├── main.py
└── README.md
```