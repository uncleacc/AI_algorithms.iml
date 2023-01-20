# import numpy as np
# from math import sqrt
#
# '''
# 用户/物品 | 物品a | 物品b | 物品c | 物品d
# 用户A     |   √  |       |   √   |
# 用户B     |   √  |   √   |       |   √
# 用户C     |   √  |   √   |   √   |   √
# '''
#
#
# # 定义余弦相似性度量计算
# def cosine(ls_1, ls_2, m):
#     Numerator = 0  # 公式中的分子
#     abs_1 = abs_2 = 0  # 分母中两向量的绝对值
#     for i in range(m):
#         Numerator += ls_1[i] * ls_2[i]
#         if ls_1[i] == 1:
#             abs_1 += ls_1[i]
#         if ls_2[i] == 1:
#             abs_2 += ls_2[i]
#     Denominator = sqrt(abs_1 * abs_2)  # 公式中的分母
#     return Numerator / Denominator
#
#
# # 定义预测函数
# def predict(w_uv, r_vi=1):
#     p = w_uv * r_vi
#     return p
#
#
# if __name__ == "__main__":
#     # 建立用户-物品矩阵
#     user_item = np.array([[1, 0, 1, 0],
#                           [1, 1, 0, 1],
#                           [1, 1, 1, 1]])
#     print("用户-物品矩阵：")
#     print(user_item)
#     user = ['用户A', '用户B', '用户C']
#     item = ['物品a', '物品b', '物品c', '物品d']
#     n = len(user)  # n个用户
#     m = len(item)  # m个物品
#     K = 1  # 只找到一个最相似用户
#
#     # 构建用户-用户相似度矩阵
#     sim = np.zeros((n, n))  # 相似度矩阵，默认全为0
#     for i in range(n):
#         for j in range(n):
#             if i < j:
#                 sim[i][j] = cosine(user_item[i], user_item[j], m)
#                 sim[j][i] = sim[i][j]
#     print("得到的用户-用户相似度矩阵：")
#     print(sim)  # 打印用户-用户相似度矩阵
#
#     # 推荐物品
#     max_sim = [0, 0, 0]  # 存放每个用户的相似用户
#     r_list = [[], [], []]  # 存放推荐给每个用户的物品
#     p = [[], [], []]  # 每个用户被推荐物品的预测值列表
#     for i in range(n):  # n个用户循环n次
#         # 找到与用户i最相似的用户
#         for j in range(n):
#             if max(sim[i]) != 0 and sim[i][j] == max(sim[i]):
#                 max_sim[i] = user[j]  # 此时的j就是相似用户的编号
#                 break  # break目的：一是结束当前循环，二是当前的j后面有用
#         if max_sim[i] == 0:
#             continue  # 等于0，表明当前用户无相似用户，无需推荐，继续下个用户
#         # 找出应该推荐的物品，并计算预测值
#         for k in range(K):  # 为了更契合预测值计算公式，因为这里K=1，所以也可以省去这个for
#             for x in range(m):  # m个物品循环m次
#                 if user_item[i][x] == 0 and user_item[j][x] == 1:  # 目标用户不知道，而相似用户知道
#                     r_list[i].append(item[x])
#                     p[i].append(predict(sim[i][j]))
#
#                     # 打印结果
#     for i in range(n):  # n个用户循环n次
#         if len(r_list[i]) > 0:  # 当前用户有被推荐的物品
#             print("向{:}推荐的物品有：".format(user[i]), end='')
#             print(r_list[i])
#             print("该用户对以上物品该兴趣的预测值为：", end='')
#             print(p[i])
#         print()
import numpy as np
from math import sqrt

'''
用户/物品 | 物品a | 物品b | 物品c 
用户A     |   √  |       |   √
用户B     |   √  |       |   √
用户C     |   √  |   √   |
'''


# 定义余弦相似性度量计算
def cosine(ls_1, ls_2, m):
    Numerator = 0  # 公式中的分子
    abs_1 = abs_2 = 0  # 分母中两向量的绝对值
    for i in range(m):
        Numerator += ls_1[i] * ls_2[i]
        if ls_1[i] == 1:
            abs_1 += ls_1[i]
        if ls_2[i] == 1:
            abs_2 += ls_2[i]
    Denominator = sqrt(abs_1 * abs_2)  # 公式中的分母
    return Numerator / Denominator


# 定义预测函数
def predict(w_uv, r_vi=1):
    p = w_uv * r_vi
    return p


if __name__ == "__main__":
    # 建立用户-物品矩阵
    user_item = np.array([[1, 0, 1, 0],  # 用户商品矩阵
                          [1, 1, 0, 1],
                          [1, 1, 1, 1]])
    print("用户-物品矩阵：")
    print(user_item)
    user = ['用户A', '用户B', '用户C']
    item = ['物品a', '物品b', '物品c', '物品d']
    n = len(user)  # n个用户
    m = len(item)  # m个物品
    K = 1  # 只找到一个最相似物品

    # 建立物品-用户倒排表
    item_user = user_item.T
    print("物品-用户矩阵：")
    print(item_user)

    # 构建物品-物品相似度矩阵
    sim = np.zeros((m, m))  # 相似度矩阵，默认全为0
    for i in range(m):
        for j in range(m):
            if i < j:
                sim[i][j] = cosine(item_user[i], item_user[j], m)
                sim[j][i] = sim[i][j]
    print("得到的物品-物品相似度矩阵：")
    print(sim)  # 打印物品-物品相似度矩阵

    # 推荐物品
    max_sim = [0, 0, 0, 0]  # 存放每个物品的相似物品
    r_list = [[], [], []]  # 存放推荐给每个用户的物品
    p = [[], [], []]  # 每个用户被推荐物品的预测值列表
    for i in range(m):  # m个物品循环m次
        # 找到与物品i最相似的物品
        for j in range(len(sim[i])):  # range()里面写m也可以
            if max(sim[i]) != 0 and sim[i][j] == max(sim[i]):
                max_sim[i] = item[j]  # 此时的j就是相似物品的编号
                break  # break目的：一是结束当前循环，二是当前的j后面有用
        if max_sim[i] == 0:
            continue  # 等于0，表明当前物品无相似物品，继续下个物品
        # 找出应该推荐的物品，并计算预测值
        for k in range(K):  # 为了更契合预测值计算公式，因为这里K=1，所以也可以省去这个for
            for x in range(n):  # n个用户循环n次
                if item_user[i][x] == 1 and item_user[j][x] == 0:  # 当前物品用户知道，而相似物品该用户不知道
                    r_list[x].append(max_sim[i])
                    p[x].append(predict(sim[i][j]))

                    # 打印结果
    for i in range(n):  # n个用户循环n次
        if len(r_list[i]) > 0:  # 当前用户有被推荐的物品
            print("向{:}推荐的物品有：".format(user[i]), end='')
            print(r_list[i])
            print("该用户对以上物品该兴趣的预测值为：", end='')
            print(p[i])
        print()