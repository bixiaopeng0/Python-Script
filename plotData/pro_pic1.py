import numpy as np
import matplotlib.pyplot as plt
x = []
x1 = []
points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/data0.txt", delimiter=",")
points1 = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/data1.txt", delimiter=",")
points2 = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/data2.txt", delimiter=",")
x = points.tolist()
x1 = points1.tolist()
x2 = points2.tolist()
right_a_hist = []
wrong_a_hist = []
right_std_hist = []
wrong_std_hist = []
right_mean_hist = []
wrong_mean_hist = []
right_con_hist = []
wrong_con_hist = []
right_a = []
wrong_a = []
right_std = []
wrong_std = []
right_mean = []
wrong_mean = []
right_con = []
wrong_con = []
all_a_hist = []

for i in range(0, len(points)):
    right_a.append(points[i,0])
    right_con.append(int(points[i,1]))
    right_mean.append(int(points[i,2]))
    right_std.append(int(points[i,3]))

for i in range(0, len(points1)):
    wrong_a.append(points1[i,0])
    wrong_con.append(int(points1[i,1]))
    wrong_mean.append(int(points1[i,2]))
    wrong_std.append(int(points1[i,3]))



for i in range(0, 200,1):
    right_a_hist.append(right_a.count(i/10))
    wrong_a_hist.append(wrong_a.count(i/10))
    # right_std_hist.append(x[i,0].count(i/10))
    # right_probability.append(x.count(i/10))
    # wrong_probability.append(x1.count(i/10))
    # all.append(x2.count(i/10))

for i in range(0,200,1):
    right_std_hist.append(right_std.count(i))
    wrong_std_hist.append(wrong_std.count(i))
    right_mean_hist.append(right_mean.count(i))
    wrong_mean_hist.append(wrong_mean.count(i))
    right_con_hist.append(right_con.count(i))
    wrong_con_hist.append(wrong_con.count(i))


plt.figure(0)
x = np.arange(0,20,0.1)
plt.title("检测 虚警直方图",FontProperties='STKAITI',fontsize=24)
# plt.ylim(0,1.1)
# plt.xlim(0,len(points),400)
plt.xlabel("α",FontProperties='STKAITI',fontsize=24)
plt.ylabel("数量",FontProperties='STKAITI',fontsize=24)
plt.plot(x,right_a_hist, color='r',label = 'True')
plt.plot(x,wrong_a_hist, color='b',label = 'Fake')
# plt.plot(x,all, color='y',label = 'ALL Point')
plt.legend(loc = 'upper left')
# plt.yticks(np.arange(0,1.1,0.1))
plt.xticks(np.arange(0,20,1))
# plt.show()

plt.figure(1)
x = np.arange(0,200,1)
plt.title("检测 虚警直方图",FontProperties='STKAITI',fontsize=24)
plt.xlabel("标准差",FontProperties='STKAITI',fontsize=24)
plt.ylabel("数量",FontProperties='STKAITI',fontsize=24)
plt.plot(x,right_std_hist, color='r',label = 'True')
plt.plot(x,wrong_std_hist, color='b',label = 'Fake')
plt.legend(loc = 'upper left')
plt.xticks(np.arange(0,200,10))
# plt.show()

plt.figure(2)
x = np.arange(0,200,1)
plt.title("检测 虚警直方图",FontProperties='STKAITI',fontsize=24)
plt.xlabel("均值",FontProperties='STKAITI',fontsize=24)
plt.ylabel("数量",FontProperties='STKAITI',fontsize=24)
plt.plot(x,right_mean_hist, color='r',label = 'Accuracy')
plt.plot(x,wrong_mean_hist, color='b',label = 'FA')
plt.legend(loc = 'upper left')
plt.xticks(np.arange(0,200,10))
# plt.show()

plt.figure(3)
x = np.arange(0,200,1)
plt.title("检测 虚警直方图",FontProperties='STKAITI',fontsize=24)
plt.xlabel("对比度",FontProperties='STKAITI',fontsize=24)
plt.ylabel("数量",FontProperties='STKAITI',fontsize=24)
plt.plot(x,right_con_hist,'r-',label = 'Accuracy')
plt.plot(x,wrong_con_hist,'b-',label = 'FA')
plt.legend(loc = 'upper left')
plt.xticks(np.arange(0,200,10))
plt.show()