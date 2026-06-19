import cv2

video = cv2.VideoCapture("cv_2/84696-586995491.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()