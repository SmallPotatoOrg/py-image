from __future__ import print_function
import os # 系统
from PIL import Image

# 执行系统命令
os.system('echo 调取系统命令') # 为调取系统的 adb 准备

# 读取图片
im = Image.open("./assets/img02.png")
w, h = im.size  # 图片的宽高
im_pixel = im.load()

# 寻找方形边界
for i in range(0, 160, 10):
    last_pixel = im_pixel[0, i]
    for j in range(290, 310, 5):
        pixel = im_pixel[j, 5]
        print(i, j, im_pixel[i, j])
        if pixel != last_pixel:
            print('pixel', i, j)
            break

print('dddd', im_pixel[150, 300])
