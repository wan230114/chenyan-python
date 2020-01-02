# -*- coding: utf-8 -*-
# @Author: ChenJun
# @Qmail:  1170101471@qq.com
# @Date:   2019-12-24 11:05:08
# @Last Modified by:   JUN
# @Last Modified time: 2019-12-24 21:38:24

"""
遍历输出嵌套字典

假如存在字典：
D = {
    1: {21: {28: {},
             29: {},
             30: {300: {301: {302: {}}}},
             32: {300: {}}},
        22: {33: {}}}, }

字典关系：
1   21  28
        29
        30  300 301 302
        32  300
    22  33

需要输出以下结果，如何实现呢？
结果：
1   21  28
1   21  29
1   21  30  300 301 302
1   21  32  300
1   22  33
"""

from pprint import pprint


def expand_values(D):
    L = []
    i = -1
    for key in D.copy():
        i += 1
        D_key_len = len(D[key])
        if i == 0:
            # print('key:', key, "len:", D_key_len)
            if not D[key]:
                L.append([key, D_key_len + 1])
                D.pop(key)
                # print('-'*50)
            else:
                L.append([key, D_key_len])
                L += expand_values(D[key])
    return L


def expand_dict(D):
    L_result = []
    # 开头处理
    # print('遍历开始：')
    L = Ltmp = expand_values(D)
    # print(L)
    L_clean = [x[0] for x in L]
    L_result.append(L_clean)
    # 循环处理
    while D:
        L = expand_values(D)  # 递归生成多个行的序列
        if L != Ltmp[:len(L)]:
            # print(L)
            L_clean = [x[0] for x in L]
            L_result.append(L_clean)
        Ltmp = L

    # print('展开结果为：')
    # pprint(L_result)
    return L_result


if __name__ == '__main__':
    D = {
        (1, 1): {
            (21, 2): {(28, 3): {},
                      (29, 3): {},
                      (30, 3): {(300, 4): {(301, 5): {(302, 6): {}}}},
                      (32, 3): {(300, 4): {}}},
            (22, 2): {(33, 3): {}}}, }
    L = expand_dict(D)
    pprint(L)
