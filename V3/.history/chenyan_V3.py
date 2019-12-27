"""
有一天平, 2克和7克砝码各一个。
若想利用天平和砝码来将140克盐分成50克和90克两份，
规定只能使用3次天平进行称量，有哪些方法？
(PS:只需要关注使用天平的次数，而非总体操作步数，
    比如沙堆合并操作，不算使用天平）


【分析：】

考虑平移的结果：

    方法9：
    [140,0,0,0]
    >1: [70, 70, 0, 0] 第1步使用天平：天平左右砝码(0,0)；
    140平分为70和70

    >2: [35, 35, 70, 0] 第2步使用天平：天平左右砝码(0,0)；
    70平分为35和35

    -*: [105, 35, 0, 0] 	沙堆合并:35与70合并得105

    >3: [50, 55, 35, 0] 第3步使用天平：天平左右砝码(7,2)；
    105平分为50和55


逻辑结构设计, 设计存储结构

n0 = {(140, 0): {}

n1 = {(140, 0): {140: {(70, 70): {}, 
                       (69, 71): {}},
      }

n2 = {(140, 0): {140: {(70, 70): {70: {(35, 35): {}, (36, 34): {}}},
                       (71, 69): {69: {(37, 32): {}, (38, 31): {}, (39, 30): {}},
                                  71: {(38, 33): {}, (39, 32): {}, (40, 31): {}}}}}}
...

"""


# %%


def fenji(shadui, f_a, f_b):
    """使用天平
    return: 沙堆1，沙堆2
    """
    # f_a + x = f_b + (140 -x)
    x = (shadui + f_b - f_a)/2
    if int(x)*2 != shadui + f_b - f_a:
        return False
    else:
        return int(x), shadui-int(x)


def fenge(shadui):
    """
    in:
        140
    out:
        {(70, 70): {}, (69, 71): {}}
    """
    D = {}
    if shadui > 0:
        for f_a, f_b in L_fs:
            fenji_result = fenji(shadui, f_a, f_b)
            if fenji_result:
                D[fenji_result] = {}
        return D
    else:
        return D


def compte_next(D_result):
    for shaduis in D_result:
        D_in = D_result[shaduis]
        for shadui in shaduis:
            fenge_result = fenge(shadui)
            if fenge_result:
                D_in[shadui] = fenge(shadui)


IN = 140
D_result = {(IN, 0): {}}

L_f = [2, 7]
L_fs = [(0, 0), (0, 2), (0, 7), (0, 9), (2, 7)]

# 第一层
from pprint import pprint
pprint(D_result)  # {(140, 0): {}}
compte_next(D_result)
pprint(D_result)  # {(140, 0): {140: {(70, 70): {}, (71, 69): {}}, 0: {}}}

for shaduis in D_result:
    for D in D_result[shaduis].values():
        if D:
            compte_next(D)
pprint(D_result)

