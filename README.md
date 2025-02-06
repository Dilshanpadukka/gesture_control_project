# Gesture-Controlled Drag and Drop System

A real-time gesture-controlled system that allows users to move virtual objects on screen using hand gestures. The system uses OpenCV and MediaPipe for hand tracking and implements intuitive drag-and-drop functionality.

## Features
- Real-time hand tracking and gesture detection
- Virtual object creation and manipulation
- Pinch-to-grab gesture recognition
- Smooth object movement and placement
- Multiple draggable objects support
- Visual feedback for interaction states

## Prerequisites
- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

## Installation
```bash
pip install -r requirements.txt
```

## Project Structure
```
gesture_drag_drop/
│
├── src/
│   ├── __init__.py
│   ├── hand_tracker.py
│   ├── virtual_object.py
│   ├── gesture_detector.py
│   └── utils.py
│
├── assets/
│   └── objects.json
│
├── requirements.txt
├── main.py
└── README.md
```

## Usage
1. Run the main script:
```bash
python main.py
```

2. Gesture Controls:
- Pinch your thumb and index finger to grab objects
- Move your hand to drag the selected object
- Release the pinch to drop the object
- Press 'q' to quit the application

## Configuration
Edit `assets/objects.json` to modify:
- Number and types of draggable objects
- Object properties (size, color, shape)
- Initial positions

## Contributing
Feel free to submit issues and enhancement requests!