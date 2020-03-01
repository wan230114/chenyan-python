"""
有一天平, 2克和7克砝码各一个。
若想利用天平和砝码来将140克盐分成50克和90克两份，
规定只能使用3次天平进行称量，有哪些方法？
(PS:只需要关注使用天平的次数，而非总体操作步数，
    比如沙堆合并操作，不算使用天平）
"""

# %%
from pprint import pprint
import itertools
import pkg_view
import pkg_expand_dict


class chenyan(object):
    def __init__(self, IN=140, TAR=50, FAMA=(2, 7), STEP=3):
        # super().__init__()
        self.IN = IN
        self.TAR = TAR
        self.STEP = STEP  # 步数
        self.FAMA = FAMA  # 砝码
        FAMAS = list(itertools.combinations(
            (0, FAMA[0], FAMA[1]), 2))+[(0, sum(FAMA))]
        # 计算左右天平存在的所有可能
        self.FAMAS = [(0, 0)] + FAMAS + [x[::-1] for x in FAMAS]
        self.D_result = {(IN, (), (), (), (), 0): {}}
        if 0:  # '测试专用':
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
            if (shadui_new > 0) and (shadui - shadui_new > 0):
                #  and (int(shadui_new)*2 == shadui + f_b - f_a):  # 去除非整数和负数结果
                shadui_new_tmp = int(shadui_new)
                shadui_new = shadui_new_tmp if shadui_new == shadui_new_tmp else shadui_new
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
        L_in = self.__get_values__(self.__compte_next__(D_result))

        # 第2, 3层
        n = 1
        while n < self.STEP:
            L_in_tmp = []
            for D_in in L_in.copy():  # 正式开始
                if D_in:
                    L_in_tmp.extend(self.__get_values__(
                        self.__compte_next__(D_in)))
            L_in = L_in_tmp
            n += 1

        # 最后一步进行最后一次不同方式合并
        L_in_tmp = []
        for d in L_in:
            for shadui_infos in d:
                if (shadui_infos[0] != self.TAR) and (shadui_infos[0] != self.IN - self.TAR):
                    # 此处需要去重，因为为了不损失信息，而又为了递归返回最后一层的方便
                    d[shadui_infos][shadui_infos] = {}
                    # 最后一层的各种合并方法
                    d[shadui_infos].update(self.__hebing__(shadui_infos))
        # 展开字典为列表。去重, 保留最后结果为50或90的
        L_result = []
        n_result = 0
        for LL in pkg_expand_dict.expand_dict(D_result):
            # if ({LL[-1][0]} | set(LL[-1][1])) & {50, 90}:
            n_result += 1
            # 第一，结果仅为50(防止90的镜像重复方法)；
            # 第二，结果可为90，但必须存在平移操作(当存在平移时不可能镜像重复)
            if (LL[-1][0] == self.TAR) or (
                    LL[-1][0] == self.IN - self.TAR
                    and [STEP for STEP in LL if STEP[2]]):
                if LL[-1] == LL[-2]:
                    LL.pop(-1)
                L_result.append(LL)
        print("共遍历到", n_result, "种称盐方法。")
        print("其中找到", len(L_result), "种符合要求的称盐方法。")  # 10717种结果
        return L_result


def main():
    # 数据初始化
    IN = 140  # 总盐
    TAR = 50  # 需要分出的盐
    FAMA = (2, 7)  # 给入两个砝码
    STEP = 3  # 限定寻找步数
    CY = chenyan(IN, TAR, FAMA, STEP)  # 初始化参数
    L_result = CY.compt()  # 计算结果
    return L_result


if __name__ == "__main__":
    L_result = main()
    pkg_view.view_text(L_result)
    pkg_view.view_png(L_result, 1)
