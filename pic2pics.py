import PIL.Image as Image
import os
import numpy as np

IMAGES_PATH = 'D:/BaiduNetdiskDownload/DongBei_University/IMAGES_1/'  # 图片集来源地址
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 200  # 每张小图片的大小
IMAGE_ROW = 3  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 3  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'D:/BaiduNetdiskDownload/DongBei_University/fixed_images_1/'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
'''
# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")
'''
# 定义图像拼接函数
def image_compose():
    images = os.listdir(IMAGES_PATH)
    i = 0;
    for img in range(1,len(images)):
        if img % 9 == 0:
            i += 8
            # to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
            mask = np.zeros((IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE), dtype='uint8')  # 这边dtype不写默认生成float64，很可能也会溢出，反正我是溢出了
            to_image = Image.fromarray(mask)
            # 循环遍历，把每张图片按顺序粘贴到对应位置上
            for y in range(1, IMAGE_ROW + 1):
                for x in range(1, IMAGE_COLUMN + 1):
                    from_image = Image.open(IMAGES_PATH + image_names[i + (IMAGE_COLUMN * (y - 1) + x - 1)]).resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
                    to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
                    to_image.save(IMAGE_SAVE_PATH + str(int(img/9)) + '.jpg')  # 保存新图
        #百分比输出
        try:
            if len(images) <= 100:
                num = 1
            elif 100 <= len(images) <= 1000:
                num = 10
            elif 1000 <= len(images) <= 10000:
                num = 100
        except ValueError:
            print("图片数量太多，请修改源程序")
        a = '*' * (img//num)
        b = '.' * ((len(images) - img)//num)
        c = ((img+1) / len(images)) * 100
        print("\r{:^3.0f}%[{}->{}]".format(c, a, b), end='')

if __name__ == '__main__':
    image_compose()
    print("图片融合完成")