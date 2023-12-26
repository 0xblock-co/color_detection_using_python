import cv2
capture = cv2.VideoCapture(0)
from identify import detect_color

if not capture.isOpened():
    print("Error: Camera is not open")
    exit()

while True:
    read, frame = capture.read()
    if read:
        cv2.imshow('Camera', frame)
        finger_detected = detect_color(frame)
        cv2.putText(frame, f'Color Detected: {finger_detected}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
