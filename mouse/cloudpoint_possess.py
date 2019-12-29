import os
import numpy as np
import sys
import cv2
import math
result=[]
clound_point_path='./car3.nvm'
Aft_Pos_CLound_path='./Aft_Pos_Clound.txt'
fr=open(clound_point_path,'r')
fw=open(Aft_Pos_CLound_path,'w')
dataMat=[]
# len=len(fr.read().split('\n'))
# a = [[0] * 6 for _ in range(31184)]
# with open(clound_point_path,'r') as f:
#     for line in f:
#       result.append(list(line.strip('\n').split(' ')))
# print(result)
# print(a)
a = []
i=0
k=0
g=0
for line in fr.readlines():
    line = line.split(' ')
    l = []
    l.append(float(line[0]))#三维点x
    l.append(float(line[1]))
    l.append(float(line[2]))
    l.append(float(line[7]))#图片序号
    l.append(float(line[9]))#二维点x
    l.append(float(line[10]))#y
    a.append(l)
#只保留图片0的特征点
x=np.array(a)
img_num = 7
for j in range(x.shape[0]):
    c=x[j][3]
    print(c)
    if c==img_num:
        g=g+1
num_list = []
print("g",g)
print(len(num_list))
for j in range(x.shape[0]):
    c=x[j][3]
    if c==img_num:
        l = []
        l.append(x[j][0])
        l.append(x[j][1])
        l.append(x[j][2])
        l.append(x[j][3])
        l.append(x[j][4])
        l.append(x[j][5])
        num_list.append(l)
#将第m行的x
# print(x)
print(num_list)
print(len(num_list))

img = cv2.imread("./car3/visualize/00000007.jpg")

for data in num_list:
    x = int(data[-2])+960
    y = int(data[-1])+540
    x3d = round(data[0],2)
    y3d = round(data[1],2)
    z3d = round(data[2],2)
    # print(data[0],x3d)
    txt = str(x3d)+":"+str(y3d)+":"+str(z3d)
    cv2.circle(img,(x,y),2,(255,255,255),0)

    # cv2.putText(img,txt,(x,y),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,255),1)
# cv2.imwrite("./save_img/car3_"+str(img_num)+".jpg",img)


def find_2dpoint(x1, y1, x2, y2):
    x_ = -1
    y_ = -1
    for data in num_list:
        x = int(data[-2]) + 960
        y = int(data[-1]) + 540
        if x >= x1 and x <= x2 and y>= y1 and y <= y2:
            x_ = x
            y_ = y
            return x_,y_

def find_3dpoint(x,y):
    for data in num_list:
        x_temp = int(data[-2]) + 960
        y_temp = int(data[-1]) + 540
        if x_temp==x and y_temp == y:
            x3d = round(data[0], 2)
            y3d = round(data[1], 2)
            z3d = round(data[2], 2)
            return x3d,y3d,z3d

def cal_3d_distance(point1,point2):
    print(point1)
    return math.sqrt(math.pow((point1[0]-point2[0]),2)+math.pow((point1[1]-point2[1]),2)+math.pow((point1[2]-point2[2]),2))

#公式
#真实
def cal_accuracy(actaul_dis,sd_dis):
    pass

num = 0
point = []
point3d = []
def draw_rectangle(event,x,y,flags,param):
    global ix, iy,num,point
    if event==cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        print("point1:=", x, y)
    elif event==cv2.EVENT_LBUTTONUP:
        print("point2:=", x, y)
        print("width=",x-ix)
        print("height=", y - iy)
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        x_p, y_p = find_2dpoint(ix,iy,x,y)
        if x_p != -1:
            num+=1
            point.append((x_p,y_p))
            point3d.append(find_3dpoint(x_p,y_p))
            if num == 1:
                cv2.putText(img,"0",(x_p+10,y_p+10),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),1)
            elif num == 2:
                cv2.putText(img,"1",(x_p+10,y_p+10),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),1)
            elif num == 3:
                cv2.putText(img,"2",(x_p+10,y_p+10),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),1)
            elif num == 4:
                cv2.putText(img, "3", (x_p+10,y_p+10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 1)
                #连线
                cv2.line(img,point[0],point[1],(255, 200, 0),2)
                cv2.line(img,point[2],point[3],(255, 200, 0),2)
                #注释
                cv2.putText(img, "Point0:(x,y):"+str(point[0][0])+" "+str(point[0][1])+"(x,y,z):"+str(point3d[0][0])+" "+str(point3d[0][1])+" "+str(point3d[0][2]), (0, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
                cv2.putText(img, "Point1:(x,y):"+str(point[1][0])+" "+str(point[1][1])+"(x,y,z):"+str(point3d[1][0])+" "+str(point3d[1][1])+" "+str(point3d[1][2]), (0, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
                cv2.putText(img, "Point2:(x,y):"+str(point[2][0])+" "+str(point[2][1])+"(x,y,z):"+str(point3d[2][0])+" "+str(point3d[2][1])+" "+str(point3d[2][2]), (0, 150), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
                cv2.putText(img, "Point3:(x,y):"+str(point[3][0])+" "+str(point[3][1])+"(x,y,z):"+str(point3d[3][0])+" "+str(point3d[3][1])+" "+str(point3d[3][2]), (0, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

                cv2.putText(img, "line1_distance:"+str(cal_3d_distance(point3d[0],point3d[1])), (0, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
                cv2.putText(img, "line2_distance:"+str(cal_3d_distance(point3d[2],point3d[3])), (0, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)



cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break