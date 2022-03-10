import cv2
import os
import numpy as np
import math

img = cv2.imread('img.jpg')
img1 = cv2.resize(img, (800,600))
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp, features = sift.detectAndCompute(gray, None)
# kps就是关键点。它所包含的信息有：
# angle：角度，表示关键点的方向
# class_id：当要对图片进行分类时，我们可以用class_id对每个特征点进行区分
# octave：代表是从金字塔哪一层提取的得到的数据
# pt：关键点点的坐标
# response：响应程度，代表该点强壮大小，更确切的说，是该点角点的程度
# size：该点直径的大小
print("pt is {}".format(kp[0].pt))
print("features is {}".format(features)+"\n"+"size is {}".format(features.shape))
print("num of kps is {}".format((len(kp))))

img1 = cv2.drawKeypoints(img1, kp, img)

for i in range(len(kp)):
    new = (int(kp[i].pt[0] - kp[i].size * math.cos(kp[i].angle)), int(kp[i].pt[1] - kp[i].size * math.sin(kp[i].angle)))
    start = (int(kp[i].pt[0]), int(kp[i].pt[1]))
    img2 = cv2.arrowedLine(img1, start, new, (0, 0, 255), thickness=1)

cv2.imshow("SIFT", img2)
cv2.waitKey(0)
# cv2.destroyAllWindows()
