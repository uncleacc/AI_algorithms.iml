import numpy as np
import math
import matplotlib.pyplot as plt


R = np.array([[5, 3, 0, 1], # 用户商品评分，0代表未参与评分
              [4, 0, 0, 1],
              [1, 1, 0, 5],
              [1, 0, 0, 4],
              [0, 1, 5, 4]])
N = R.shape[0]  # 用户数
M = R.shape[1]  # 商品数
K = 5           # 主题数
# 定义P和Q矩阵
P = np.random.rand(N, K)    # 初始化P和 Q
Q = np.random.rand(K, M)

def getLoss(R, P, Q, N, M, K, beta):    # 损失函数
    loss = 0.
    for i in range(N):
        for j in range(M):
            if (R[i][j] == 0):
                continue
            sum = sum2 = 0
            for k in range(K):
                sum += P[i][k] * Q[k][j]
                sum2 += P[i][k] * P[i][k] + Q[k][j] * Q[k][j]
            loss += math.pow(R[i][j] - sum, 2) + beta * sum2 / 2
    return loss
def matrix_composition(R, P, Q, N, M, K, alpha = 0.0002, beta = 0.002): # 矩阵分解
    loss_list = []
    for step in range(5000):    # 规定梯度下降次数
        loss = getLoss(R, P, Q, N, M, K, beta)
        if(loss < 0.001):   # 损失值可以忽略不计
            break
        if(step % 20 == 0): # 每20次记录一下loss变化
            plt.scatter(step, loss)
        # if(step % 1000 == 0):   # 调试
        #     print(loss)
        # update
        for i in range(N):
            for j in range(M):
                if(R[i][j] == 0):   # 只看有评分的
                    continue
                sum = 0
                for k in range(K):
                    sum += P[i][k] * Q[k][j]
                for k in range(K):  # 更新变量
                    P[i][k] += alpha * (2 * (R[i][j] - sum) * Q[k][j] - beta * P[i][k])
                    Q[k][j] += alpha * (2 * (R[i][j] - sum) * P[i][k] - beta * Q[k][j])
    return P, Q



if __name__ == '__main__':
    print('评分矩阵')
    print(R)
    P, Q = matrix_composition(R, P, Q, N, M, K)
    print('P和Q矩阵如下')
    print(P)
    print()
    print(Q)
    print()
    print(np.dot(P, Q)) # 矩阵计算
    plt.show()