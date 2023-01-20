import numpy as np
from math import sqrt


user_item = np.array([[1, 0, 1, 0],     # 用户商品矩阵
                      [1, 1, 0, 1],
                      [1, 1, 1, 1]])
item_user = user_item.T         # 商品用户矩阵
user_num = user_item.shape[0]   # 用户数
item_num = user_item.shape[1]   # 商品数
user_mat = np.empty((user_num, user_num))   # 用户相似度矩阵
item_mat = np.empty((item_num, item_num))   # 商品相似度矩阵
sim = []    # 和每个用户最相似的用户编号
sim2 = []   # 和每个商品最相似的商品编号
user_rem_item = [[], [], []]    # 给每个用户推荐的商品
user_rem_sco = [[], [], []]     # 给每个用户推荐商品对应评分
user_name = ['用户一', '用户二', '用户三']   # 打印对应名字
item_name = ['物品一', '物品二', '物品三', '物品四']

def cosine(ls1, ls2):   # 余弦相似度
    fz = np.sum(ls1 * ls2)
    fm = sqrt(np.linalg.norm(ls1) * np.linalg.norm(ls2))    # 模长api
    return fz / fm

def predict(w_uv, r_vs = 1):    # 评分预测
    return w_uv * r_vs

if __name__ == '__main__':
    # 打印商品物品矩阵
    print(user_item)
    print()

    # 基于用户CF
    for i in range(user_num):   # 计算用户相似度
        for j in range(user_num):
            if(i < j):
                user_mat[i][j] = cosine(user_item[i], user_item[j])
                user_mat[j][i] = user_mat[i][j]
            elif (i == j):
                user_mat[i][j] = 0
    print('用户相似矩阵：')
    print(user_mat)
    for i in range(user_num):
        for j in range(user_num):
            if(user_mat[i][j] == max(user_mat[i])):     # 找最匹配的用户
                for k in range(item_num):
                    if(user_item[i][k] == 0 and user_item[j][k] == 1):  # 别人喜欢，指定用户还没看到的商品
                        user_rem_item[i].append(k)  # 推荐
                        user_rem_sco[i].append(predict(user_mat[i][j])) # 给它打分
                sim.append(j)  # 加入最相似的列表
                break

    # 基于商品CF
    for i in range(item_num):   # 计算商品相似度
        for j in range(item_num):
            if(i < j):
                item_mat[i][j] = cosine(item_user[i], item_user[j])
                item_mat[j][i] = item_mat[i][j]
            elif(i == j):
                item_mat[i][j] = 0
    print('商品相似矩阵：')
    print(item_mat)
    for i in range(item_num):
        for j in range(item_num):
            if(item_mat[i][j] == max(item_mat[i])):     # 找最匹配的商品
                for k in range(user_num):
                    if(user_item[k][i] == 0 and user_item[k][j] == 1):  # 此用户喜欢一个商品，还没看到相似商品
                        user_rem_item[k].append(i)  # 推荐
                        user_rem_sco[k].append(predict(item_mat[i][j])) # 给它打分
                sim2.append(j)  # 加入最相似的列表
                break   # 只找最相似的一个

    # 打印推荐结果
    print()
    # 商品最相似结果
    # for i in range(item_num):
    #     print('和{}最相似的是{}'.format(item_name[i],item_name[sim2[i]]))
    for i in range(user_num):   # 打印结果
        print('给{}其推荐的商品如下：'.format(user_name[i]))
        for j in range(len(user_rem_item[i])):
            if(j != len(user_rem_item[i])-1):   # 打印格式，处理最后的逗号
                print('{}({})'.format(item_name[user_rem_item[i][j]],user_rem_sco[i][j]), end='，')
            else:
                print('{}({})'.format(item_name[user_rem_item[i][j]],user_rem_sco[i][j]))
        print()

