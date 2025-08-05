import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (choose 'yolov8n.pt', 'yolov8s.pt', etc.)
model = YOLO('yolov8n.pt')

def main():
    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Inference
        results = model(frame)

        # Render results
        annotated_frame = results[0].plot()

        # Display the resulting frame
        cv2.imshow('YOLOv8 Detection', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when job is finished
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()