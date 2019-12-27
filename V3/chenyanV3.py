"""
有一天平, 2克和7克砝码各一个。
若想利用天平和砝码来将140克盐分成50克和90克两份，
规定只能使用3次天平进行称量，有哪些方法？
(PS:只需要关注使用天平的次数，而非总体操作步数，
    比如沙堆合并操作，不算使用天平）


【分析：】
三种基本操作：
    平分，平移，合并

数据存储的逻辑结构：

    # 当前沙堆 , 分出沙堆 , 平移 , 平分 , 合并 , 天平使用次数
    D = {(140, (), (fa), (fa), (fa), 0):{}}

        fa = ((a1,-a2), ((b1,b2),+a2))
            a1 -- 左砝码
            a2 -- 左边用沙堆当做的砝码
            b1 -- 右砝码
            b2 -- 右边用沙堆当做的砝码

"""

# %%
from pprint import pprint
import itertools

try:
    import expand_dict as ed
except:
    import os
    os.chdir('V3')
    import expand_dict as ed


class chenyan(object):
    def __init__(self, IN=140, TAR=50, FAMA=(2, 7), STEP=3):
        # super().__init__()
        self.IN = IN
        self.TAR = TAR
        self.STEP = STEP
        self.FAMA = FAMA  # 砝码
        self.FAMAS = [(0, 0),
                      (0, 2), (2, 0),
                      (0, 7), (7, 0),
                      (0, 9), (9, 0),
                      (2, 7), (7, 2)]
        self.D_result = {(IN, (), (), (), (), 0): {}}
        if not '测试专用':
            # shadui_infos = (115, (9, 16), (), (), (), 2)
            # d = self.__pingyi__(shadui_infos)
            # pprint(d)
            # d = self.__pingfen__(shadui_infos)
            # pprint(d)
            # d = self.__hebing__(shadui_infos)
            # pprint(d)
            shadui_infos = (127, (2, 2, 9), ((0, -9), (7, 2)), (), (), 3)
            print(shadui_infos)
            pprint(self.__hebing__(shadui_infos))

    def __pingyi__(self, shadui_infos):
        """方法1：平移"""
        D = {}
        S_pianyi = set()
        shadui, shengyu, pingyi, pingfen, hebing, step = shadui_infos
        for f in self.FAMAS:
            for shengyu_x in (0,)+shengyu:
                pianyi = f[1] + shengyu_x - f[0]
                if pianyi > 0 and pianyi not in S_pianyi:
                    S_pianyi.add(pianyi)
                    shadui_new = shadui - pianyi
                    if shadui_new > 0:
                        shadui_infos_new = (shadui_new,
                                            shengyu+(pianyi,),
                                            ((-f[0], -pianyi),
                                             (f[1], shengyu_x)),
                                            (),
                                            (),
                                            step+1)
                        D[shadui_infos_new] = {}
        # pprint(D)
        return D

    def __pingfen__(self, shadui_infos):
        """方法2：平分"""
        D = {}
        shadui, shengyu, pingyi, pingfen, hebing, step = shadui_infos
        for f in self.FAMAS:
            f_a, f_b = f
            shadui_new = (shadui + f_b - f_a)/2
            if (shadui_new > 0) and (shadui - shadui_new > 0) and (
                    int(shadui_new)*2 == shadui + f_b - f_a):  # 去除非整数和负数结果
                shadui_new = int(shadui_new)
                # print(f, shadui, shadui_new)
                shadui_infos_new = (shadui_new,
                                    shengyu+(shadui-shadui_new,),
                                    (),
                                    (shadui, (-f[0], -shadui_new),
                                     (-f[1], -(shadui-shadui_new))),
                                    (),
                                    step+1)
                D[shadui_infos_new] = {}
        # pprint(D)
        return D

    def __hebing__(self, shadui_infos):
        """方法3：合并"""
        D = {}
        shadui, shengyu, pingyi, pingfen, hebing, step = shadui_infos
        # shengyu = (1, 2, 3, 4)  # 调试数据
        L = list(shengyu)[:-1]
        # 合并
        if L:
            # 主线及分线的两种合并方式，主必须有shadui，副则任两及之上
            for INDEX_shadui, value in enumerate((shadui, shengyu[-1])):
                if INDEX_shadui == 0:
                    L_hebing = []
                    for i in range(1, len(L)+1):
                        L_hebing += list(itertools.combinations(L, i))
                    for i, x in enumerate(L_hebing):
                        L_hebing[i] = (shadui,) + x
                elif INDEX_shadui == 1:
                    L_hebing = []
                    for i in range(2, len(L)+1):
                        L_hebing += list(itertools.combinations(shengyu, i))
                S_hebing = set()
                for t_hebing in L_hebing:
                    # print(t_hebing, S_hebing)
                    shadui_sums = sum(t_hebing)
                    shadui_new = shadui_sums if INDEX_shadui == 0 else shadui
                    if shadui_sums not in S_hebing:
                        S_hebing.add(shadui_sums)
                        L_shengyu = list(shengyu)
                        iters = t_hebing[1:] if INDEX_shadui == 0 else t_hebing
                        shengyu_INDEX1 = (
                            shadui_sums,) if INDEX_shadui == 1 else ()
                        for x in iters:
                            # print(x, 'removing in', L_shengyu)
                            L_shengyu.remove(x)
                        shadui_infos_new = (shadui_new,
                                            tuple(L_shengyu) + shengyu_INDEX1,
                                            (),
                                            (),
                                            (t_hebing, shadui_sums),
                                            step)
                        D[shadui_infos_new] = {}
                        # print(shadui_infos_new, '\n')
        return D

    def __compte_next__(self, D_result):
        """通过此层字典计算下一层字典
                沙堆 可合并 天平
        in : {((140), (), (), (), 1): {}}
        out: {((140), (), (), (), 1): {
                ((70), (70), (), (), 1): {},
                ((69), (71), (), (), 1): {},
                ((71), (69), (), (), 1): {},
            }
        """
        for shadui_infos in D_result:
            # 处理平移
            D_result[shadui_infos].update(self.__pingyi__(shadui_infos))
            # 处理平分
            D_result[shadui_infos].update(self.__pingfen__(shadui_infos))
            # 合并之后进行平移、平分，使得当前分支最底层步数保持一致
            hebing_result = self.__hebing__(shadui_infos)
            D_result[shadui_infos].update(hebing_result)
            if hebing_result:
                for hebing_info in hebing_result:
                    D_doing = D_result[shadui_infos][hebing_info]
                    # 处理平移
                    D_doing.update(self.__pingyi__(hebing_info))
                    # 处理平分
                    D_doing.update(self.__pingfen__(hebing_info))
        return D_result

    def __get_values__(self, D):
        """返回字典每一个分支的最后一个元素的列表"""
        L = []
        for key in D:
            if not D[key]:
                L.append({key: D[key]})
            else:
                L.extend(self.__get_values__(D[key]))  # 利用递归求最后一个元素
        return L

    def compt(self):
        # 第1层
        D_result = self.D_result
        # pprint(D_result)
        L_in = self.__get_values__(self.__compte_next__(D_result))
        # pprint(D_result)

        # 第2, 3层
        n = 1
        while n < self.STEP:
            # print(n)
            # pprint(L_in)
            L_in_tmp = []
            # 正式开始
            for D_in in L_in.copy():
                if D_in:
                    L_in_tmp.extend(self.__get_values__(
                        self.__compte_next__(D_in)))
            L_in = L_in_tmp
            n += 1
        # 最后一步进行最后一次不同方式合并
        L_in_tmp = []
        for d in L_in:
            for shadui_infos in d:
                if (shadui_infos[0] != self.TAR) and (shadui_infos[0] != self.IN-self.TAR):
                    # 此处需要去重，因为为了不损失信息，而又为了递归返回最后一层的方便
                    d[shadui_infos][shadui_infos] = {}
                    # 最后一层的各种合并方法
                    d[shadui_infos].update(self.__hebing__(shadui_infos))
        # 展开字典为列表
        L = ed.expand_dict(D_result)
        # for LL in L:
        #     print(*LL, sep=" | ")
        # return
        # print(len(L))  # 10717种结果
        # 去重, 保留最后结果为50或90的
        L_result = []
        for LL in L:
            # 第一，结果仅为50(防止90的镜像重复方法)；
            # 第二，结果可为90，但必须存在平移操作(当存在平移时不可能镜像重复)
            if (LL[-1][0] == self.TAR) or (
                    LL[-1][0] == self.IN - self.TAR
                    and [LL_step for LL_step in LL if LL_step[2]]):
                if LL[-1] == LL[-2]:
                    LL.pop(-1)
                L_result.append(LL)
        return L_result


def view(L_result):
    for i_m, LL in enumerate(L_result):
        print('\n方法%s：' % (i_m+1))
        i = 0
        while i < len(LL)-1:
            i += 1
            shadui, shengyu, pingyi, pingfen, hebing, step = LL[i]
            # print(LL[i])
            if hebing:
                print('-* 合并：沙堆【{}】合并为【{}】'.format(
                    str(hebing[0])[1:-1], hebing[1]
                ))
            else:
                if pingyi:
                    method = "平移"
                    s1, s2, s3, s4 = (pingyi[0][0],
                                      pingyi[0][1],
                                      pingyi[1][0],
                                      pingyi[1][1])
                elif pingfen:
                    method = "平分"
                    s1, s2, s3, s4 = (pingfen[1][0],
                                      pingfen[1][1],
                                      pingfen[2][0],
                                      pingfen[2][1]
                                      )
                print('-> 第{}步, {method}, 【{:>3}】-->【 {:>3} + {:>3} 】, '
                      '天平【左:{:>+3}g砝码{:>+3}g沙堆, 右:{:>+3}g砝码{:>+3}g沙堆】'.format(
                          step, LL[i-1][0], shadui, shengyu[-1],
                          s1, s2, s3, s4, method=method
                      ))


def main():
    # 数据初始化
    IN = 140  # 总盐
    TAR = 50  # 需要分出的盐
    FAMA = (2, 7)
    STEP = 3
    CY = chenyan(IN, TAR, FAMA, STEP)
    L_result = CY.compt()
    return L_result


if __name__ == "__main__":
    L_result = main()
    # import sys
    # sys.exit()
    view(L_result)
