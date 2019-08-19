import numpy as np
import matplotlib.pyplot as plt

right = []
fake = []
y0_low = []
y0_high = []
y1_low = []
y1_high = []

# points = np.genfromtxt("G:/19/lab/C++/drone/detectionRate/code/Project1/Project1/std.txt", delimiter=",")
points = np.genfromtxt("G:/19/lab/python/drone_ssd/scr/mian.txt", delimiter=",")

for i in range(0, len(points)):
    # if i % 2 == 0
    right.append(points[i, 0])
    fake.append(points[i, 1])


print("1",right.count(1))
print("0",right.count(0))
print(sum(fake))
x = np.arange(len(right))
# plt.subplot(4,1,1)
plt.title("直方图",FontProperties='STKAITI',fontsize=24)
#plt.ylim(0,1.1)
plt.xlim(0,len(points))
plt.yticks(np.arange(0,1.1,1))
plt.xticks(np.arange(0,len(right),100))
plt.ylabel("数量",FontProperties='STKAITI',fontsize=24)
plt.xlabel("帧数",FontProperties='STKAITI',fontsize=24)
plt.plot(x,right, 'b-',label = 'TP')
plt.legend(loc = 'best')
plt.show()

