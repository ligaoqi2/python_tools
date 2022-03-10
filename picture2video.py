import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image

# video路径中请务必包含.mp4的str，否则程序运行无结果

def Pic2Video(imgPath,videoPath):
    # imgPath = "D:/BaiduNetdiskDownload/DongBei_University/IMAGES/"  # 读取图片路径
    # videoPath = "D:/BaiduNetdiskDownload/DongBei_University/video.mp4"  # 保存视频路径
    images = os.listdir(imgPath)
    fps = 3  # 每秒3帧数
    # VideoWriter_fourcc为视频编解码器 ('I', '4', '2', '0') —>(.avi) 、('P', 'I', 'M', 'I')—>(.avi)、('X', 'V', 'I', 'D')—>(.avi)、('T', 'H', 'E', 'O')—>.ogv、('F', 'L', 'V', '1')—>.flv、('m', 'p', '4', 'v')—>.mp4
    fourcc = VideoWriter_fourcc(*"mp4v")
    image = Image.open(imgPath + images[0])
    videoWriter = cv2.VideoWriter(videoPath, fourcc, fps, image.size)
    print("需要转为视频的图片总数为{}张".format(len(images)))
    for im_name in range(len(images)):
        frame = cv2.imread(imgPath + images[im_name])  # 这里的路径只能是英文路径
        # frame = cv2.imdecode(np.fromfile((imgPath + images[im_name]), dtype=np.uint8), 1)  # 此句话的路径可以为中文路径
        # print("正在传输第{}张图片".format(im_name))
        #百分比输出start
        try:
            if len(images) <= 100:
                num = 1
            elif 100 <= len(images) <= 1000:
                num = 10
            elif 1000 <= len(images) <= 10000:
                num = 100
        except ValueError:
            print("图片数量太多，请修改源程序")
        a = '*' * (im_name//num)
        b = '.' * ((len(images) - im_name)//num)
        c = (im_name / len(images)) * 100
        print("\r{:^3.0f}%[{}->{}]".format(c, a, b), end='')
        #百分比输出over
        videoWriter.write(frame)
    print("\n图片转视频已完成！")
    videoWriter.release()
    cv2.destroyAllWindows()

'''
def Video2Pic():
    videoPath = "./res.mp4"  # 读取视频路径
    imgPath = "jpg/"  # 保存图片路径

    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    while suc:
        frame_count += 1
        suc, frame = cap.read()
        # cv2.imwrite(imgPath + str(frame_count).zfill(4), frame)
        cv2.imwrite(imgPath + "%d.jpg" % frame_count, frame)
        cv2.waitKey(1)
    cap.release()
    print("视频转图片结束！")
'''

if __name__ == '__main__':
    imgPath = "D:/BaiduNetdiskDownload/DongBei_University/fixed_images_1/"  # 读取图片路径
    videoPath = "D:/BaiduNetdiskDownload/DongBei_University/video1.mp4"  # 保存视频路径
    Pic2Video(imgPath,videoPath)
