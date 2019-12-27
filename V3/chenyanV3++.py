# %%
from pprint import pprint
from graphviz import Digraph
import os
try:
    os.chdir('V3')
    import chenyanV3
except:
    import chenyanV3

# os.makedirs('Result-png', exist_ok=True)
# os.chdir('Result-png')


L_result = chenyanV3.main()
chenyanV3.view(L_result)

gz = Digraph("result", 'comment', None, None, 'png', None, "UTF-8",
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
i_m_max = len(L_result)
for i_m, LL in enumerate(L_result[::-1]):
    # i_m += 1
    i_m = i_m_max - i_m
    # print('\n方法%s：' % i_m)

    GZ_name_last = '%02d_00_0' % (i_m)
    # print(GZ_name_last, 140)
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
        # print(LL[i])
        if hebing:
            # print('-* 合并：沙堆【{}】合并为【{}】'.format(
                # str(hebing[0])[1:-1], hebing[1]
            # ))
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
            # print('-> 第{}步, {method}, 【{:>3}】-->【 {:>3} + {:>3} 】, '
                #   '天平【左:{:>+3}g砝码{:>+3}g沙堆, 右:{:>+3}g砝码{:>+3}g沙堆】'.format(
                #   step, LL[i-1][0], shadui, shengyu[-1],
                #   s1, s2, s3, s4, method=method
                #   ))
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
# print(gz.source)
gz.view()
