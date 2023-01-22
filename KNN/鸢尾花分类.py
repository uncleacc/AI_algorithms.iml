import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from math import sqrt

##### 数据准备 ####
iris = pd.read_csv('E:\Python\Iris.csv')
num_iris = len(iris)
#将 3 种类型分别映射为 0,1,2
iris["type"] = iris["type"].map({"Iris-setosa":0,"Iris-versicolor":1,"Iris-virginica":2})
#定义一个测试集
test_data = [[5.5,5.2,7.0,5.6],[3.6,2.3,2.9,3.2]]#[[花萼长度]，[花萼宽度]]，一共四个测试数据
print("测试数据：")
print("花萼长度：",end='')
print(test_data[0])
print("花萼宽度：",end='')
print(test_data[1])

##### 数据整理 #####
iris_0 = [[],[]]
iris_1 = [[],[]]
iris_2 = [[],[]]#分别对应三种鸢尾花，两个子列表分别存储前两列的数据
iris_type = iris.type
for i in range(num_iris):
    if iris_type[i] == 0:
        iris_0[0].append(iris.sl[i])
        iris_0[1].append(iris.sw[i])
    elif iris_type[i] == 1:
        iris_1[0].append(iris.sl[i])
        iris_1[1].append(iris.sw[i])
    else:
        iris_2[0].append(iris.sl[i])
        iris_2[1].append(iris.sw[i])

#####KNN 对测试集进行分类 ######
#定义欧氏距离
def Euclid(x1,y1,x2,y2):
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    return d

def _KNN_(x,y):
    K = 5
    #====== 计算距离 =======#
    distance_0 = []
    distance_1 = []
    distance_2 = []
    distances = []
    #计算并记录距离
    for i in range(50):
        d = Euclid(x,y,iris_0[0][i],iris_0[1][i])
        distance_0.append(d)
    for i in range(50):
        d = Euclid(x,y,iris_1[0][i],iris_1[1][i])
        distance_1.append(d)
    for i in range(50):
        d = Euclid(x,y,iris_2[0][i],iris_2[1][i])
        distance_2.append(d)
    #由小到大排序（此处使用冒泡排序）
    distances = distance_0 + distance_1 + distance_2
    for i in range(len(distances)-1):
        for j in range(len(distances)-i-1):
            if distances[j] > distances[j+1]:
                distances[j],distances[j+1]=distances[j+1],distances[j]
    #======== 决策划分 ========#
    #定义删除函数，避免对同一个数据重复计算
    def delete(a,b,ls):
        for i in range(b):
            if ls[i] == a:
                ls.pop(i)
                break
    #找出与测试数据最接近的 K 个点
    number_0 = number_1 = number_2 = 0
    for i in range(K):
        if distances[i] in distance_0:
            number_0 += 1
            delete(distances[i],len(distance_0),distance_0)
            continue
        if distances[i] in distance_1:
            number_1 += 1
            delete(distances[i],len(distance_1),distance_1)
            continue
        if distances[i] in distance_2:
            number_2 += 1
            delete(distances[i],len(distance_2),distance_2)
            continue

    max_number = max(number_0,number_1,number_2)
    if max_number == number_0:
        return 0
    elif max_number == number_1:
        return 1
    else:
        return 2

print("这四个测试数据分别属于:")
for i in range(len(test_data[0])):
    m=_KNN_(test_data[0][i],test_data[1][i])
    if m == 0:
        print("Iris-setosa")
    elif m == 1:
        print("Iris-versicolor")
    else:
        print("Iris-virginica")

##### 画图 #####
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#训练集
plt.scatter(iris_0[0],iris_0[1],marker='o',label='Iris-setosa',color='blue')
plt.scatter(iris_1[0],iris_1[1],marker='x',label='Iris-versicolor',color='black')
plt.scatter(iris_2[0],iris_2[1],marker='s',label='Iris-virginica',color='green')
#测试集
plt.scatter(test_data[0],test_data[1],marker='^',label='测试数据',color='red')
plt.legend()
plt.show()