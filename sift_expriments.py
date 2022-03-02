import cv2
import os
import numpy as np

img = cv2.imread('img.jpg')
img1 = cv2.resize(img, (800,600))
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp, features = sift.detectAndCompute(gray, None)
print("features is {}".format(features)+"\n"+"size is {}".format(features.shape))
print("num of kps is {}".format((len(kp))))

# for i in range(len(kp)):
#     print("第{0}个特征点坐标是{1}".format(i, str(int(kp[i].pt[0])), str(int(kp[i].pt[1])))+"\t"+"特征点方向的角度是{}".format(str(int(kp[i].angle))))

img1 = cv2.drawKeypoints(img1, kp, img)
cv2.imshow("SIFT", img1)
cv2.waitKey(0)
# cv2.destroyAllWindows()
