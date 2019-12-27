while 1:
  # 将上次进行平移的对象进行步数同步
  p = 0
   for d_tmp in L_in:
        D_in_tmp = {}
        # print('-->', d_tmp)
        for key in d_tmp.copy():
            if key[-1] < n:
                D_in_tmp[key] = d_tmp.pop(key)
                p = 1
        if D_in_tmp:
            L_in.extend(
                get_values(compte_next(D_in_tmp)))
    if p:
        continue
