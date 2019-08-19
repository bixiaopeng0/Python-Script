import numpy as np
import matplotlib.pyplot as plt

right_probability = []
wrong_probability = []
std = []
mean = []
add = []
con = []
y0_low = []
y0_high = []
y1_low = []
y1_high = []

points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/data.txt", delimiter=",")

for i in range(0, len(points)):
    right_probability.append(points[i, 0])
    wrong_probability.append(points[i, 1])
    std.append(points[i,2])
    mean.append(points[i,3])
    add.append(points[i,2]/points[i,3])
    con.append(points[i,4])
    y0_low.append(0.1)
    y0_high.append(0.8)
    y1_low.append(0.4)
    y1_high.append(0.6)

x = np.arange(len(points))
print(right_probability)
# plt.subplot(4,1,1)
plt.title("检测率 虚警率",FontProperties='STKAITI',fontsize=24)
# plt.ylim(0,1.1)
plt.xlim(0,len(points))

plt.ylabel("概率",FontProperties='STKAITI',fontsize=24)
plt.xlabel("帧数",FontProperties='STKAITI',fontsize=24)
plt.plot(x,y0_low, color='r',ls='--')
plt.plot(x,y0_high, color='r',ls='--')
plt.plot(x,y1_low, color='y',ls='--')
plt.plot(x,y1_high, color='y',ls='--')
plt.plot(x,right_probability, color='k',label = 'P')
plt.plot(x,wrong_probability, color='b',label = 'WP')
plt.legend(loc = 'best')
# plt.subplot(4,1,2)
# plt.ylabel("方差",FontProperties='STKAITI',fontsize=24)
# plt.plot(x,std)
# plt.subplot(4,1,3)
# plt.ylabel("均值",FontProperties='STKAITI',fontsize=24)
# plt.plot(x,mean,color = 'g')
# # plt.subplot(5,1,2)
# # plt.plot(x,add,color='r')
# plt.subplot(4,1,4)
# plt.xlabel("帧数",FontProperties='STKAITI',fontsize=24)
# plt.plot(x,con,color='r')
# plt.ylabel("对比度",FontProperties='STKAITI',fontsize=24)
#
# # plt.yticks(np.arange(0,1.1,0.1))
# plt.xticks(np.arange(0,len(points),300))
plt.show()