# -*- coding: utf-8 -*-
# @Author: ChenJun
# @Qmail:  1170101471@qq.com
# @Date:   2019-12-24 21:05:08
# @Last Modified by:   wan230114
# @Last Modified time: 2019-12-24 21:31:13

"""
遍历嵌套字典
字典关系：
1   21  31
        30  300 301 302
        32  300
    22  33

输出结果：
1   21  28
1   21  29
1   21  30  300 301 302
1   21  32  300
1   22  33
"""

from pprint import pprint


def expand_values(D):
    L = []
    for i, key in enumerate(D.copy()):
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


def fmain(D):
    L_result = []
    # 开头处理
    print('遍历开始：')
    L = Ltmp = expand_values(D)
    print(L)
    L_clean = [x[0] for x in L]
    L_result.append(L_clean)
    # 循环处理
    while D:
        L = expand_values(D)  # 递归生成多个行的序列
        if L != Ltmp[:len(L)]:
            print(L)
            L_clean = [x[0] for x in L]
            L_result.append(L_clean)
        Ltmp = L

    print('展开结果为：')
    pprint(L_result)


if __name__ == '__main__':
    D = {
        (1): {
            (21): {(28): {},
                   (29): {},
                   (30): {300: {301: {302: {}}}},
                   (32): {300: {}}},
            (22): {(33): {}}}, }
    L = fmain(D)
