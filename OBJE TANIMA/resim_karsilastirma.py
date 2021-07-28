import cv2
import numpy as np

path1 = "C:\\Users\\Kader\\Desktop\\OBJE TANIMA\\test_images\\aircraft.jpg"
path2 = "C:\\Users\\Kader\\Desktop\\OBJE TANIMA\\test_images\\aircraft1.jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(640,550))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(640,550))

img3 = cv2.medianBlur(img1,7)

"""
if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")
"""

# diff = difference
diff = cv2.subtract(img1,img3)
b,g,r = cv2.split(diff)

#devamı var