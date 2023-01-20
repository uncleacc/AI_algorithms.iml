import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib


matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 画布显示中文字体简黑
data = pd.read_csv('data.txt', header=None)
data = np.array(data)
m = data.shape[0]
X = data[:,0]
Y = data[:,1]
plt.plot(X, Y, 'k+', label = '数据')  # ‘颜色+点的形状+线的形状’
plt.xlabel('面积')
plt.ylabel('房价')
plt.title('梯度下降')
# print(X, Y)
theta = [0, 0]

def cost(X, Y, theta):  # 损耗函数
    yTemp = X * theta[1] + theta[0] # 得出直线上在x坐标下的y
    return np.sum((yTemp - Y) ** 2) / (2 * m)

def gradient(X, Y, theta):
    res = np.empty(len(theta))
    yTemp = X * theta[1] + theta[0]
    res[0] = np.sum(yTemp - Y) / m
    res[1] = np.sum((yTemp - Y) * X) / m
    return res

def gradient_descent(X, Y, theta, eta):
    while(True):
        lastTheat = theta
        grd = gradient(X, Y, theta)
        theta = theta - grd * eta
        if(abs(cost(X, Y, theta) - cost(X, Y, lastTheat)) < 1e-15):
            break
    return theta

if __name__ == '__main__':
    ans = gradient_descent(X, Y, theta, 0.001)
    x = np.array([2, 25])
    y = ans[0] + ans[1] * x
    plt.plot(x, y, c = 'r', label = '拟合线')
    plt.legend()
    plt.show()
