import numpy as np
import matplotlib.pyplot as plt

right_probability = []
wrong_probability = []
y0_low = []
y0_high = []
y1_low = []
y1_high = []

# points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/std.txt", delimiter=",")
# points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/a.txt", delimiter=",")
points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/detect_frames.txt", delimiter=",")

for i in range(0, len(points)):
    # if i % 2 == 0
    right_probability.append(points[i, 0])
    wrong_probability.append(points[i, 1])
    y0_low.append(0.1)
    y0_high.append(0.8)
    y1_low.append(0.4)
    y1_high.append(0.6)

# x = range
# x = np.arange(1,len(points)/2+1,0.5)
# x = np.arange(0,len(points)/10,0.1)
x = np.arange(1,len(points)+1,1)
print(right_probability)
print(len(points))


plt.title("检测率 虚警率",FontProperties='STKAITI',fontsize=24)
plt.ylim(0,1.1)
plt.xlim(1,len(points)+1,1)
# plt.xlabel("标准差阈值",FontProperties='STKAITI',fontsize=24)
# plt.xlabel("α阈值",FontProperties='STKAITI',fontsize=24)
plt.xlabel("检测帧数",FontProperties='STKAITI',fontsize=24)
plt.ylabel("概率",FontProperties='STKAITI',fontsize=24)
plt.plot(x,y0_low, "r",ls='--')
plt.plot(x,y0_high, color='r',ls='--')
plt.plot(x,y1_low, color='y',ls='--')
plt.plot(x,y1_high, color='y',ls='--')
plt.plot(x,right_probability, 'k*-',label = 'P')
plt.plot(x,wrong_probability, 'b*-',label = 'WP')
plt.legend(loc = 'best')
plt.yticks(np.arange(0,1.05,0.05))
# plt.xticks(np.arange(1,19,0.5))
plt.xticks(np.arange(1,len(points)+1,1))
plt.show()