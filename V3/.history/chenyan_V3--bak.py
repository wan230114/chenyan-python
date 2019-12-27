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

L0   = ((140),(),())
L1_1 = ((70, 70),(0,0),())
L1_2 = ((35, 35, 70),(0,0),()))
L2_n = ((15, 20, 35, 70),(2,7),()))

n0 = {L0:{}}

n0 = {L0:{
          L1_1:{},
          L1_2:{}
         }
     }

n0 = {L0:{
          L1_1:{L2_n:{}, L2_n:{}},
          L1_2:{}
         }
     }

n3 = 

...

"""


# %%
from pprint import pprint


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
        { ((70, 70),(0,0),())):{}, 
          ((69, 71),(0,2),())):{} }
    """
    D = {}
    if shadui > 0:
        for f in L_fs:
            fenji_result = fenji(shadui, f[0], f[1])
            if fenji_result:
                fenji_result.append(f, ())
                D[fenji_result] = {}
        return D
    else:
        return D


def compte_next(D_result):
    for L_lujing in D_result:
        L_lujing_new = L_lujing.copy()
        Ln_last = L_lujing[-1]
        for shadui in set(Ln_last[0]):
            Ln_nexts = fenge(shadui)
            if Ln_nexts:
                for Ln in Ln_nexts:
                    pass


def compte_next(D_result):
    for shaduis in D_result:
        D_in = D_result[shaduis]
        for shadui in shaduis:
            fenge_result = fenge(shadui)
            if fenge_result:
                D_in[shadui] = fenge(shadui)


IN = 140
Ln = ((IN), (), ())
D_result = {Ln: {}}


# L_f = [2, 7]
L_fs = [(0, 0), (0, 2), (0, 7), (0, 9), (2, 7)]

# 第一层
pprint(D_result)
compte_next(D_result)
pprint(D_result)

for shaduis in D_result:
    for D in D_result[shaduis].values():
        if D:
            compte_next(D)
pprint(D_result)
