#camera calibration
import numpy as np
import cv2
import glob
# 终止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 准备对象点， 如 (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:9].T.reshape(-1,2)
# 用于存储所有图像的对象点和图像点的数组。
objpoints = [] # 真实世界中的3d点
imgpoints = [] # 图像中的2d点
images = glob.glob('C:/Users/Adiministor/Desktop/calibrationtemplate/*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 找到棋盘角落
    ret, corners = cv2.findChessboardCorners(gray, (6,9), None)
    # 如果找到，添加对象点，图像点（细化之后）
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # 绘制并显示拐角
        cv2.drawChessboardCorners(img, (6,9), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
#cv.destroyAllWindows()
#camera libration
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
#print("ret: \n",ret)
print("内参矩阵mtx: \n",mtx) #内参矩阵
print("畸变系数dist: \n",dist)#畸变系数
print("旋转矩阵rvecs: \n",rvecs)
print("平移向量tvecs: \n",tvecs)
"""
#矫正函数
def undistortion(img,mtx,dist):
    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # 剪裁图像
    #x, y, w, h = roi
    #dst = dst[y:y+h, x:x+w]
    cv2.imshow('calibrationresult', dst)
############################调用函数###########################################
img = cv2.imread('C:/Users/Adiministor/Desktop/picture/anquantao1.jpg')
undistortion(img,mtx,dist)
"""



