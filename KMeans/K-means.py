import matplotlib.pyplot as plt
from random import uniform
from math import sqrt
import numpy as np


data = [[], []]
n = 50
for i in range(n):
    if i < 20:
        data[0].append(uniform(0, 4))
        data[1].append(uniform(0, 12))
    elif i >= 20 and i < 30:
        data[0].append(uniform(0, 10))
        data[1].append(uniform(0, 10))
    else:
        data[0].append(uniform(9, 12))
        data[1].append(uniform(0, 12))
plt.scatter(data[0], data[1], marker='+')
plt.show()
plt.xlim(0, 12)
plt.ylim(0, 12)
cent = np.empty((3, 2)) # 创建中心
for i in range(3):  # 随机初始化中心
    cent[i][0] = uniform(0, 12)
    cent[i][1] = uniform(0, 12)
dist = np.empty((3, n)) # 距离中心的距离

def distEuclid(x1, y1, x2, y2): # 计算欧几里得距离
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

def k_means():  # k-means算法
    for step in range(50):
        for i in range(n):
            for j in range(3):  # 计算距离
                dist[j][i]=distEuclid(data[0][i], data[1][i], cent[j][0], cent[j][1])
        sumX = [0, 0, 0]    # 记录距离每一个中心最近的点X和
        sumY = [0, 0, 0]    # 记录距离每一个中心最近的点Y和
        num = [0, 0, 0]     # 记录距离每一个中心最近的点数量
        for i in range(n):
            mi = min(dist[0][i], dist[1][i], dist[2][i])
            for j in range(3):
                if(dist[j][i] == mi):
                    sumX[j] += data[0][i]   # update
                    sumY[j] += data[1][i]
                    num[j] += 1
                    if(step == 49): # 最后一次分配画图
                        c = ''
                        if (j == 0):
                            c = 'g'
                        elif (j == 1):
                            c = 'b'
                        else:
                            c = 'r'
                        plt.scatter(data[0][i], data[1][i], marker='+', color=c)
        for i in range(3):  # 更新中心坐标
            cent[i][0] = sumX[i] / num[i]
            cent[i][1] = sumY[i] / num[i]
    for i in range(3):  # 画中心
        plt.scatter(cent[i][0], cent[i][1], marker='*', c='k')
    plt.show()


if __name__ == '__main__':
    k_means()
