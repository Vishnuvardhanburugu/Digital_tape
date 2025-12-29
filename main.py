import cv2
import numpy as np

raw_img = cv2.imread("Digital_tape/raw_images/raw1.jpg")

if raw_img is None:
    raise FileNotFoundError("Image not found")

width, height = raw_img.shape[:2]

cv2.imwrite("Digital_tape/input_images/reference1.jpg", raw_img)

print(f"Wall Width: {width:.2f} mm")
print(f"Wall Height: {height:.2f} mm")
