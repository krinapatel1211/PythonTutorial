import cv2
import numpy as np
import pytesseract
import os

# C:\Program Files (x86)\Tesseract-OCR

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img1 = cv2.imread('Query_Unfilled.png')
h, w, c = img1.shape
# img1 = cv2.resize(img1, (w, h))

orb = cv2.ORB_create(5000)
kp1, desc1 = orb.detectAndCompute(img1, None)
# impKp1 = cv2.drawKeypoints(img1, kp1, None)

# cv2.imshow('KeyPointsQuery', impKp1)
cv2.imshow('Output', img1)
cv2.waitKey(0)


