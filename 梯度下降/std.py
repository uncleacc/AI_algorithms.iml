# 房屋价格与面积
# 序号：1     2    3    4     5     6     7
# 面积：150  200  250  300   350   400   600
# 价格：6450 7450 8450 9450 11450 15450 18450

import matplotlib.pyplot as plt
import matplotlib
from math import pow
from random import uniform
import random

x0 = [150, 200, 250, 300, 350, 400, 600]
y0 = [6450, 7450, 8450, 9450, 11450, 15450, 18450]
# # 为了方便计算，将所有数据缩小100倍
x = [1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 6.00]
y = [64.50, 74.50, 84.50, 94.50, 114.50, 154.50, 184.50]
# 线性回归函数为 y=theta0+theta1*x
# 参数定义
theta0 = 0.1  # 对theata0赋值
theta1 = 0.1  # 对theata1赋值
alpha = 0.1  # 学习率
m = len(x)
count0 = 0
theta0_list = []
theta1_list = []

# 使用批量梯度下降法
for num in range(10000):
    count0 += 1
    diss = 0  # 误差
    deriv0 = 0  # 对theata0导数
    deriv1 = 0  # 对theata1导数
    # 求导
    for i in range(m):
        deriv0 += (theta0 + theta1 * x[i] - y[i]) / m
        deriv1 += ((theta0 + theta1 * x[i] - y[i]) / m) * x[i]
    # 更新theta0和theta1
    for i in range(m):
        theta0 = theta0 - alpha * ((theta0 + theta1 * x[i] - y[i]) / m)
        theta1 = theta1 - alpha * ((theta0 + theta1 * x[i] - y[i]) / m) * x[i]
    # 求损失函数J(θ)
    for i in range(m):
        diss = diss + (1 / (2 * m)) * pow((theta0 + theta1 * x[i] - y[i]), 2)

    theta0_list.append(theta0 * 100)
    theta1_list.append(theta1)
    # 如果误差已经很小，则退出循环
    if diss <= 0.001:
        break

theta0 = theta0 * 100  # 前面所有数据缩小了100倍，所以求出的theta0需要放大100倍，theta1不用变

# 使用随机梯度下降法
theta2 = 0.1  # 对theata2赋值
theta3 = 0.1  # 对theata3赋值
count1 = 0
theta2_list = []
theta3_list = []

for num in range(10000):
    count1 += 1
    diss = 0  # 误差
    deriv2 = 0  # 对theata2导数
    deriv3 = 0  # 对theata3导数
    # 求导
    for i in range(m):
        deriv2 += (theta2 + theta3 * x[i] - y[i]) / m
        deriv3 += ((theta2 + theta3 * x[i] - y[i]) / m) * x[i]
    # 更新theta0和theta1
    for i in range(m):
        theta2 = theta2 - alpha * ((theta2 + theta3 * x[i] - y[i]) / m)
        theta3 = theta3 - alpha * ((theta2 + theta3 * x[i] - y[i]) / m) * x[i]
    # 求损失函数J(θ)
    rand_i = random.randrange(0, m)
    diss = diss + (1 / (2 * m)) * pow((theta2 + theta3 * x[rand_i] - y[rand_i]), 2)

    theta2_list.append(theta2 * 100)
    theta3_list.append(theta3)
    # 如果误差已经很小，则退出循环
    if diss <= 0.001:
        break
theta2 = theta2 * 100

# print("批量梯度下降最终得到theta0={}，theta1={}".format(theta0, theta1))
# print("           得到的回归函数是：y={}+{}*x".format(theta0, theta1))
# print("随机梯度下降最终得到theta0={}，theta1={}".format(theta2, theta3))
# print("           得到的回归函数是：y={}+{}*x".format(theta2, theta3))
# 画原始数据图和函数图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(x0, y0, 'bo', label='数据', color='black')
print(x0, y0)
plt.plot(x0, [theta0 + theta1 * x for x in x0], label='批量梯度下降', color='red')
# plt.plot(x0, [theta2 + theta3 * x for x in x0], label='随机梯度下降', color='blue')
plt.xlabel('x（面积）')
plt.ylabel('y（价格）')
plt.legend()
plt.show()
# plt.scatter(range(count0), theta0_list, s=1)
# plt.scatter(range(count0), theta1_list, s=1)
# plt.xlabel('上方为theta0，下方为theta1')
# plt.show()
# plt.scatter(range(count1), theta2_list, s=3)
# plt.scatter(range(count1), theta3_list, s=3)
# plt.xlabel('上方为theta0，下方为theta1')
# plt.show()