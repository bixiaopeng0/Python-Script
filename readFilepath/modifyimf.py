import os
import cv2
import numpy as np
path = "./img/"
path1 = "G:/19/lab/C++/drone/doc/data/单帧检测-随机点/2019-07-02_080246.png"
str = []
#listdir 返回path路径下的文件
dirs = os.listdir(path)

for dir in dirs:
    #将文件名和后缀名分隔开
    if(os.path.splitext(dir)[1] == '.jpg' or os.path.splitext(dir)[1] == '.png'):
        str.append(dir)

print(str)
for i in str:
    img = cv2.imdecode(np.fromfile(path1, dtype=np.uint8), -1)#解决imerad读取中文命名问题
    # img = cv2.imread(path+i)
    # print(path+i)
    print(path1)
    x, y = img.shape[0:2]
    print(x,y)
    img=cv2.resize(img,(int(y/2),int(x/2)))
    cv2.imshow("scr",img)
    cv2.imencode('.jpg', img)[1].tofile(path1)#解决imwrite写中文命名问题
    # cv2.imwrite(path+i,img)
    cv2.waitKey(10)