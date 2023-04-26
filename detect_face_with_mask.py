import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    cv2.imshow("Resultado", frame)

    key = cv2.waitKey(1)

    if key == 32:
        print("Fechando")
        break

video.release()