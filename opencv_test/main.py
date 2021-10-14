# -*- coding: utf-8 -*-
import numpy as np
import cv2


if __name__ == '__main__':
    cap = cv2.VideoCapture(-1)  # 노트북 웹캠을 카메라로 사용
    cap.set(3, 640)  # 너비
    cap.set(4, 480)  # 높이

    ret, frame = cap.read()  # 사진 촬영
    frame = cv2.flip(frame, 1)  # 좌우 대칭

    cv2.imwrite('picture/test.jpg', frame)  # 사진 저장

    cap.release()
    cv2.destroyAllWindows()