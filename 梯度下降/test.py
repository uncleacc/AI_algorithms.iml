import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv('hourse_price.txt', header=None)
data = np.array(data)
m = data.shape[0]
X = data[:,0]
Y = data[:,1]
plt.scatter(X, Y, marker='+')
X = X / 100
Y = Y / 100
# print(X, Y)
theta = [0.1, 0]

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
    cnt = 0
    while(True):
        cnt += 1
        if(cnt >= 1000000): break;
        lastTheat = theta
        grd = gradient(X, Y, theta)
        theta = theta - grd * eta
        if(abs(cost(X, Y, theta) - cost(X, Y, lastTheat)) < 0.001):
            break
    return theta

if __name__ == '__main__':
    ans = gradient_descent(X, Y, theta, 0.0001)
    ans[0] *= 100
    x = np.array([120, 600])
    y = ans[0] + ans[1] * x
    plt.plot(x, y, c = 'r')
    plt.show()
