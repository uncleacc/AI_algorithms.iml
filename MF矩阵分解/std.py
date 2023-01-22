import numpy as np
import math
import matplotlib.pyplot as plt


# 定义矩阵分解函数
def Matrix_decomposition(R, P, Q, N, M, K, alpha=0.0002, beta=0.02):
    Q = Q.T  # Q矩阵转置
    loss_list = []  # 存储每次迭代计算的loss值
    for step in range(5000):
        loss = 0.0
        # 计算每一次迭代后的loss大小，就是原来R矩阵里面每个非缺失值跟预测值的平方损失
        for i in range(N):
            for j in range(M):
                if R[i][j] != 0:
                    # 计算loss公式加号的左边
                    data = 0
                    for k in range(K):
                        data = data + P[i][k] * Q[k][j]
                    loss = loss + math.pow(R[i][j] - data, 2)
                    # 得到完整loss值
                    for k in range(K):
                        loss = loss + beta / 2 * (P[i][k] * P[i][k] + Q[k][j] * Q[k][j])
                    loss_list.append(loss)
        plt.scatter(step, loss)
        # 输出loss值
        if (step + 1) % 1000 == 0:
            print("loss={:}".format(loss))
        # 判断
        if loss < 0.001:
            print(loss)
            break

        # 更新R^
        for i in range(N):
            for j in range(M):
                if R[i][j] != 0:
                    # 计算损失函数
                    error = R[i][j]
                    for k in range(K):
                        error -= P[i][k] * Q[k][j]
                    # 优化P,Q矩阵的元素
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * error * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * error * P[i][k] - beta * Q[k][j])
    plt.show()
    return P, Q


if __name__ == "__main__":
    N = 5
    M = 4
    K = 5
    R = np.array([[5, 3, 0, 1],
                  [4, 0, 0, 1],
                  [1, 1, 0, 5],
                  [1, 0, 0, 4],
                  [0, 1, 5, 4]])  # N=5,M=4
    print("初始评分矩阵：")
    print(R)
    # 定义P和Q矩阵
    P = np.random.rand(N, K)  # N=5,K=2
    Q = np.random.rand(M, K)  # M=4,K=2
    print("开始矩阵分解：")
    P, Q = Matrix_decomposition(R, P, Q, N, M, K)
    print("矩阵分解结束。")
    print("得到的预测矩阵：")
    print(np.dot(P, Q))