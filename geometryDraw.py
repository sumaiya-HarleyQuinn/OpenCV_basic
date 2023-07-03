import cv2
import numpy as np

img = cv2.imread('Pictures/girl.jpg', 1)

img = cv2.line(img, (0, 0), (100, 500), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (200, 200), (500, 500), (0, 255, 0), 10)
img = cv2.rectangle(img, (300, 0), (400, 120), (255, 0, 0), -1)
img = cv2.circle(img, (351, 56), 59, (25, 99, 0), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV' ,(10, 500), font, 4, (255, 255, 255), 5, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()