# YOLO-Object-Detection-App

This application uses [YOLOv8](https://github.com/ultralytics/ultralytics) for real-time object detection via your webcam.

## Features

- Real-time object detection using your webcam
- Utilizes the YOLOv8 model (`yolov8n.pt` by default)
- Displays detected objects with bounding boxes and labels

## Requirements

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Ultralytics YOLO](https://pypi.org/project/ultralytics/)

## Installation

1. Clone this repository and navigate to the project directory.
2. Install dependencies:
    ```sh
    pip install opencv-python ultralytics
    ```
3. Ensure the `yolov8n.pt` model file is present in the project directory.

## Usage

Run the application with:

```sh
python yolo_webcam.py
```

- A window will open showing your webcam feed with detected objects.
- Press `q` to quit.

## File Structure

- [`yolo_webcam.py`](yolo_webcam.py): Main application script.
- [`yolov8n.pt`](yolov8n.pt): YOLOv8 model weights.
- [`README.md`](README.md): Project documentation.

