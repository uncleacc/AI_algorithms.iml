from operator import attrgetter
import matplotlib.pyplot as plt
import matplotlib
from math import sqrt


class point:
    def __init__(self, kind, dis):
        self.kind = kind
        self.dis = dis

#####初始化数据集#####
data_A = [[1,2],[3.2,4],[4,7],[5.2,3],[7,4.1]]#数据集A
data_B = [[2.2,5.5],[4.2,2],[5,5],[6.3,7]]#数据集B
test_data = [[4.5,4.5], [1, 2]]#测试集
num_A = len(data_A)
num_B = len(data_B)
num_T = len(test_data)

def getDis(p1, p2):
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

# calc dist
def calcDist():
    lsDist = [[], []]
    ls = []
    for i in range(len(test_data)):
        for j in range(num_A):
            lsDist[i].append(point(0, getDis(data_A[j], test_data[i])))
            ls.append(getDis(data_A[j], test_data[i]))
        for j in range(num_B):
            lsDist[i].append(point(1, getDis(data_B[j], test_data[i])))
            ls.append(getDis(data_B[j], test_data[i]))

    return lsDist, ls

def judge(k, lsDist):
    num0 = 0
    num1 = 0
    for j in range(len(test_data)):
        for i in range(k):
            if(lsDist[j][i].kind == 0):
                num0 += 1
            else:
                num1 += 1
        if(num0 > num1):
            print('A类')
        else:
            print('B类')

def draw():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    for i in range(num_A-1):
        plt.plot(data_A[i][0], data_A[i][1], 'r^')
    plt.plot(data_A[num_A-1][0], data_A[num_A-1][1], 'r^', label='A')
    for i in range(num_B-1):
        plt.plot(data_B[i][0], data_B[i][1], 'bo')
    plt.plot(data_B[num_B-1][0], data_A[num_B-1][1], 'bo', label='B')
    for i in range(num_T-1):
        plt.plot(test_data[i][0], test_data[i][1], 'k+')
    plt.plot(test_data[num_T-1][0], test_data[num_T-1][1], 'k+', label = '未标识')
    plt.legend()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.show()

def printf(lsDist):
    for j in range(len(lsDist)):
        for i in range(len(lsDist[j])):
            print('({},{})'.format(lsDist[j][i].dis, lsDist[j][i].kind))

if __name__ == '__main__':
    lsDist, ls = calcDist()
    print('距离列表')
    printf(lsDist)
    for i in range(len(lsDist)):
        lsDist[i] = sorted(lsDist[i], key=attrgetter('dis'))
    print('排序后的距离列表')
    printf(lsDist)
    k = int(input('请输入k：'))
    judge(k, lsDist)
    draw()