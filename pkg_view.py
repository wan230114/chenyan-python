"""
本模块功能为之前计算数据的可视化展示（文本描述或图形可视化）
"""


def view_text(L_result):
    """数据结果输出打印文本描述"""
    for i_m, LL in enumerate(L_result):
        print('\n方法%s：' % (i_m+1))
        i = 0
        while i < len(LL)-1:
            i += 1
            shadui, shengyu, pingyi, pingfen, hebing, step = LL[i]
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


def view_png(L_result, isALL=1):
    """数据可视化为流程图

    Arguments:
        L_result {list} -- 输入的结果列表

    Keyword Arguments:
        isALL {int} -- 控制是否只生成一张图 (default: {1})
    """
    from graphviz import Digraph

    def getGZobj(GZ_file_name):
        """获取创建gz对象"""
        gz = Digraph(GZ_file_name, 'comment', None, None, 'png', None, "UTF-8",
                     {'rankdir': 'LR'},
                     {'color': 'black',
                      'fontcolor': 'black',
                      # 'fontname': 'Consolas',
                      # 'fontname': 'FangSong',
                      'fontsize': '12',
                      'style': 'rounded',
                      'shape': 'box'},
                     {'color': '#999999',
                      'fontcolor': '#888888',
                      'fontsize': '10',
                      # 'fontname': 'FangSong'
                      },
                     None,
                     False)
        return gz
    if isALL:
        gz = getGZobj('result')
    i_m_max = len(L_result)
    for i_m, LL in enumerate(L_result[::-1]):
        i_m = i_m_max - i_m  # i_m += 1
        # print('\n方法%s：' % i_m)
        GZ_name_last = '%02d_00_0' % (i_m)
        if not isALL:
            gz = getGZobj('method%02d' % i_m)
        gz.node(GZ_name_last, 'method%2d: \n140' % i_m)
        d_shengyu = {140: GZ_name_last}  # 用来存储node和对应数值之间的关系，用于调试显示当前结果
        i = 0
        last_step = 0
        while i < len(LL)-1:
            i += 1
            shadui, shengyu, pingyi, pingfen, hebing, step = LL[i]
            if step != last_step:
                i_num = 1
                last_step = step
            d_gz_node = {'color': 'red', 'fontcolor': 'red'
                         } if shadui in (50, 90) else {}
            # ({shadui} | set(shengyu)) & TAR_seed
            # print(LL[i])
            if hebing:
                GZ_name_now = '%02d_%d_%d' % (i_m, step, i_num)
                i_num += 1
                gz.node(GZ_name_now, str(hebing[1]), d_gz_node)
                d_shengyu[GZ_name_now] = hebing[1]
                GZ_name_last = GZ_name_now
                for x in hebing[0]:
                    # print(GZ_name_last, '-->', GZ_name_now, x)
                    gz.edge(d_shengyu[x], GZ_name_now)
            else:
                if pingyi:
                    s1, s2, s3, s4 = (pingyi[0][0],
                                      pingyi[0][1],
                                      pingyi[1][0],
                                      pingyi[1][1])
                elif pingfen:
                    s1, s2, s3, s4 = (pingfen[1][0],
                                      pingfen[1][1],
                                      pingfen[2][0],
                                      pingfen[2][1]
                                      )
                GZ_name_now = '%02d_%d_%d' % (i_m, step, i_num)
                i_num += 1
                GZ_name_now2 = '%02d_%d_%d' % (i_m, step, i_num)
                i_num += 1
                d_shengyu[shadui] = GZ_name_now
                d_shengyu[shengyu[-1]] = GZ_name_now2
                # print(GZ_name_last, '--->', GZ_name_now, shadui)
                # print(GZ_name_last, '--->', GZ_name_now2, shengyu[-1])
                gz.node(GZ_name_now, str(shadui), d_gz_node)
                gz.node(GZ_name_now2, str(shengyu[-1]))
                gz.edge(GZ_name_last, GZ_name_now, '(%+3d,%+3d)' % (s1, s2))
                gz.edge(GZ_name_last, GZ_name_now2, '(%+3d,%+3d)' % (s3, s4))
                GZ_name_last = GZ_name_now
        if not isALL:
            gz.view(directory='result-PNGs')
    if isALL:
        # print(gz.source)
        gz.view()


if __name__ == "__main__":
    import chenyanV3
    L_result = chenyanV3.main()
    view_text(L_result)  # 称盐流程文本描述输出
    view_png(L_result, 0)   # 称盐流程可视化
