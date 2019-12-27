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
from expand_dict import expand_dict
from pprint import pprint


def fenji(shadui, f_a, f_b):
    """天平称量的具体操作
    return: 沙堆1，沙堆2 / False
    in:  140  2  0
    out: 69  71
    """
    # f_a + x = f_b + (140 -x)
    x = (shadui + f_b - f_a)/2
    if int(x)*2 != shadui + f_b - f_a:
        return False
    else:
        return int(x), shadui-int(x)


def fenge(shadui, shengyu, n):
    """计算天平称量平分的所有可能结果
    in:
        140
    out:
        {((70, 70), (), (0, 0), 1): {},
         ((69, 71), (), (0, 2), 1): {}}
    """
    D = {}
    if shadui > 0:
        for f in L_fs:
            fenji_result = fenji(shadui, f[0], f[1])
            if fenji_result:
                fenji_result = (
                    fenji_result[0],
                    shengyu+(fenji_result[1],),
                    f,
                    n)
                D[fenji_result] = {}
        return D
    else:
        return D


def pingyi():
    """计算合并(平移)的操作
    in:
        115, (9, 16),  2
    out:
        {(90, (9, 16, 25,), (), 3): {}},
         ( , (39,), (), 3): {}},
          }

    目的，解决如下计算方式：
        方法22：
        [140,0,0,0]
        >1: [131, 9, 0, 0] 第1步使用天平：天平左右砝码(0,9)；
        140平移为131和9
        >2: [115, 16, 9, 0] 第2步使用天平：天平左右砝码(0,16)；
        131平移为115和16
        （16g=7g砝码+9g沙堆）
        >3: [90, 25, 16, 9] 第3步使用天平：天平左右砝码(0,25)；
        115平移为90和25
        （25g=9g砝码+16g沙堆）

    打造如下计算方式：
        [(140, (), (), 0),
        (9, (131,), (0, 9), 1),
        (16, (115, 9), (0, 7), 2),
        (25, (115, ), (), 2),
        (50, (70, 20), (0, 25), 3)]

        [(140, (), (), 0),
        (131, (9,), (0, (9)), 1),
        (115, (9, 16), (0, (9, 7)), 2),
        (115, (25), (), 2),
        (90, (25, 25), (0, (25,)), 2)]
    """
    pass


def hebing(shadui, shengyu, n):
    """计算合并(平移)的操作
    in:
        32, (69, 39),  2
    out:
        {(101, (39,), (), 2): {}}}
    """
    D = {}
    shengyu = list(shengyu)
    if shadui > 0:
        for shengyu_n in shengyu[:-1]:
            L_shengyu = shengyu.copy()
            L_shengyu.remove(shengyu_n)
            fenji_result = (shadui+shengyu_n,
                            tuple(L_shengyu),
                            (),
                            n)
            D[fenji_result] = {}
        return D
    else:
        return D


def compte_next(D_result):
    """通过此层字典计算下一层字典
             沙堆 可合并 天平
    in : {((140, 0), (), (), 1): {}}
    out: {((140, 0), (), (), 1): {140: {((70, 70), (0, 0), (), 2): {},
                                        ((71, 69), (0, 2), (), 2): {}}}}
    """
    for shaduis_info in D_result:
        # print(shaduis_info)
        shadui, shengyu, tianpin, n = shaduis_info
        D_in = D_result[shaduis_info]
        # 处理平分
        fenge_result = fenge(shadui, shengyu, n+1)
        if fenge_result:
            D_in.update(fenge_result)
        # 处理平移
        hebing_result = hebing(shadui, shengyu, n)
        if hebing_result:
            for hebing_info in hebing_result:
                # print('\nhebing_info', hebing_info)
                p_shadui, p_shengyu, p_tianpin, p_n = hebing_info
                fenge_result = fenge(p_shadui, p_shengyu, p_n+1)
                # print('fenge_result', fenge_result)
                if fenge_result:
                    hebing_result[hebing_info].update(fenge_result)
            D_in.update(hebing_result)
    return D_result


def get_values(D):
    """返回字典每一个分支的最后一个元素的列表"""
    L = []
    for key in D:
        if not D[key]:
            L.append({key: D[key]})
        else:
            L.extend(get_values(D[key]))  # 利用递归求最后一个元素
    return L


def fmain():
    # 数据初始化
    IN = 140  # 总盐
    TAR = 50  # 需要分出的盐
    D_result = {(IN, (), (), 0): {}}

    global L_fs
    L_f = [2, 7]  # 砝码
    L_fs = [(0, 0),
            (0, 2), (0, 7), (0, 9), (2, 7),
            (2, 0), (7, 0), (9, 0), (7, 2)]

    # 第1层
    # pprint(D_result)
    L_in = get_values(compte_next(D_result))
    # pprint(D_result)

    # 第2, 3层
    n = 1
    while n < 3:
        # print(n)
        # pprint(L_in)
        L_in_tmp = []
        # 正式开始
        for D_in in L_in.copy():
            if D_in:
                L_in_tmp.extend(
                    get_values(compte_next(D_in)))
        L_in = L_in_tmp
        n += 1

    # 对最后一次平分的值进行合并操作
    L = get_values(D_result)
    for x in range(n):
        for d_tmp in L.copy():
            for shaduis_info in d_tmp:
                shadui, shengyu, tianpin, n = shaduis_info
                if shadui != TAR:
                    hebing_result = hebing(shadui, shengyu, n)
                    if hebing_result:
                        d_tmp[shaduis_info].update(hebing_result)
        L = get_values(D_result)
    # pprint(D_result)  # 此处可以看到所有的结果

    # 展开字典
    L = expand_dict(D_result)
    # 筛选结果
    L_filter = [LL for LL in L if LL[-1][0] == TAR]
    # pprint(L_filter)
    # print(len(L_filter))
    return L_filter


if __name__ == "__main__":
    L_filter = fmain()
    for i_m, LL in enumerate(L_filter):
        print('\n方法%s：' % (i_m+1))
        i = 0
        while i < len(LL)-1:
            i += 1
            shadui, shengyu, tianpin, step = LL[i]
            if tianpin:
                print('-> 第{}步, 沙堆【{}】平分为【{} + {}】, 天平【{}, {}】'.format(
                    step, LL[i-1][0], shadui, shengyu[-1], tianpin[0], tianpin[1])
                )
            else:
                print('-* 合并：沙堆【{}】与【{}】合并为【{}】'.format(
                    LL[i-1][0], shadui-LL[i-1][0], shadui
                ))
