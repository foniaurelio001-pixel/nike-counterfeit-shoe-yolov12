from ultralytics import YOLO
import cv2

model = YOLO("best (1).pt")
cap = cv2.VideoCapture(1)
print("🎥 Live detection running... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.5, verbose=False)[0]
    annotated = results.plot()
    cv2.imshow("Nike Counterfeit Detector - YOLOv12", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()