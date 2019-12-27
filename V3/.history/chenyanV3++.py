#%%
from pprint import pprint
from graphviz import Digraph
import os
# os.chdir("V3")
import chenyanV3


gz = Digraph("result", 'comment', None, None, 'png', None, "UTF-8",
             {'rankdir': 'TB'},
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

for i_m, LL in enumerate(chenyanV3.fmain()):
    i_m += 1
    print('\n方法%s：' % i_m)
    pprint(LL)
    last_shadui = '%02d_00_0' % (i_m)
    print(last_shadui, 140)
    gz.node(last_shadui, '140')
    d_shengyu = {}
    i = 0
    while i < len(LL)-1:
        i += 1
        i_num = 1
        shadui, shengyu, tianpin, step = LL[i]

        d_gz_node = {'color': 'red', 'fontcolor': 'red'} if shadui == 50 else {}
        if tianpin:
            for t, x in zip(tianpin, [shadui, shengyu[-1]]):
                now_shadui = '%02d_%d_%d' % (i_m, step, i_num)
                print(last_shadui, '-->', now_shadui, x, t)
                gz.node(now_shadui, str(x), d_gz_node)
                d_gz_node = {}
                gz.edge(last_shadui, now_shadui, str(t))
                i_num += 1
            print('-> 第{}步, 沙堆【{}】平分为【{} + {}】, 天平【{}, {}】'.format(
                step, LL[i-1][0], shadui, shengyu[-1], tianpin[0], tianpin[1])
            )
            d_shengyu[x] = now_shadui
            last_shadui = '%02d_%d_%d' % (i_m, step, 1)
        else:
            pingyi_shadui = '%02d_%d_%d_p' % (i_m, step, i_num)
            print(last_shadui, '-->', pingyi_shadui)
            print(d_shengyu[shadui-LL[i-1][0]], '-->', pingyi_shadui)
            gz.node(pingyi_shadui, str(shadui), d_gz_node)
            gz.edge(last_shadui, pingyi_shadui)
            gz.edge(d_shengyu[shadui-LL[i-1][0]], pingyi_shadui)
            print('-* 平移：沙堆【{}】与【{}】合并为【{}】'.format(
                LL[i-1][0], shadui-LL[i-1][0], shadui
            ))
            last_shadui = pingyi_shadui

print(gz.source)
# gz.view()
gz.view(quiet=True)
