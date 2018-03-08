#!/usr/bin/python
# -*- coding: cp936 -*-

shu = 1     ##当前找出的方法

print '天平称盐程序:'
print '  有一个天平,2克和7克砝码各一个,'
print '  若利用天平砝码将140克盐分成50,90克两份,'
print '  规定只能使用3次天平进行称量，有哪些方法？'

##*******确定天平，fml和fmr*******
def F(x1,x2,x3,x4,nn):
    A = [9,7,2,0]  ##若改为[0,2,7,9]，则结果以90为点出发
    B = [0,2,7,9]
    cpL = []
    dbALL=[x1,x2,x3,x4]
    n=nn    ##当前循环已经进行完了第n步
    for dbA in A:
##        print '【1】for dbA in A:'
        ALL = dbALL[:]
    ##    确定fml
        fml = dbA
    ##    确定fmr的数组
        if fml==0: B = [0,2,7,9]
        if fml==2: B = [0,7]
        if fml==7: B = [0,2]
        if fml==9: B = [0]
    ##    确定fmr
        for dbB in B:
##            print '【2】for dbB in B:'
            f1_ALL = ALL[:]  ##;print f1_ALL
            FMR=[]
            FMR.append([dbB,0])
            n_fmr=1
            while n_fmr <= n: 
                if f1_ALL[n_fmr]>0:
                    dbB_x=dbB+f1_ALL[n_fmr] ##;print dbB,dbB_x
                    FMR.append([dbB_x,1]) ##数组列表存储合并指标“1”
                n_fmr+=1
            for db_FMR in FMR:
##                print '【3】while n_FMR<len(FMR):'
                f2_ALL = f1_ALL[:]
                fmr = db_FMR[0]
                fmki= db_FMR[1]   ##给定沙堆与砝码合并与否的指标,程序设计后期可去掉优化
    ##*******运算程序*******
                x = f2_ALL[0]
                y = 0   ##;print 'fm:',fml,fmr,fmki
                Y=[]
                if fml < fmr:
                    y = x-(fmr-fml)
                    Y.append([y,1])     ##方法，1平移，2平分；y:结果y(x)
                if fmki==0:             ##合并了沙堆做砝码的不能参与平分
                    y = (x+fmr+fml)*0.5-fml;
                    if int(y)==y:
                        y=int(y)
                    Y.append([y,2])
    ##*******记录程序*******
                for db_Y in Y:
##                    print '【4】for db_Y in Y:'
                    f3_ALL=f2_ALL[:]
                    if db_Y[0]<=0:
                        continue ##y值不符合时进入下一个循环
                    f3_ALL[0] = db_Y[0]
                    n_next = n
##                    print 'n',n,'',f3_ALL
                    while n_next>0:
                        f3_ALL[n_next+1] = f3_ALL[n_next]
                        n_next = n_next - 1
                    f3_ALL[1] = x - f3_ALL[0]
    ##*******沙堆合并操作*******
                    HB=[[f3_ALL[0],0,0,0]]  ##HB=[合并后y，1代表已经合并，合并前x，合并的第几个数指标]
                    if n>=1:
                        n_hb = 1            ##合并的第几个数指标
                        while n_hb <= 3:    ##Y[n_result]##为后续n步操作改进做准备
                            if f3_ALL[n_hb]<=0:n_hb+=1;continue;
                            hb=f3_ALL[0] + f3_ALL[n_hb];
                            HB.append([ hb , 1 , f3_ALL[n_hb] , n_hb ])
                            n_hb += 1  ##; if hb==109: print HB
                    for db_HB in HB:
##                        print '【5】for db_HB in HB:'
                        f4_ALL=f3_ALL[:]  ##;print '1',f4_ALL[0],'2',db_HB[0]
                        f4_ALL[0]=db_HB[0]
                        if db_HB[1]==1:
                            f4_ALL[db_HB[3]]=0
                        ##至此，完成第n步
                        db_L = [f4_ALL[:]]
                        db_L.extend((n+1, [fmki, dbB, fml , fmr], [db_Y[1], x  , db_Y[0]], [db_HB[1],f3_ALL[0],f4_ALL[0]],f3_ALL))
                        cpL.append(db_L)
    return cpL

##打印，解析函数
def P1(n,hbi,hbx,hby,outALL):
    if n==1:
        print '>1:',L1[5],'第1步使用天平：天平左右砝码(%d,%d)；'%(L1[2][2],L1[2][3])
        P2(L1[3][0],L1[3][1],L1[3][2],L1[2][0],L1[2][1],L1[2][3])
        P3(hbi,hbx,hby,outALL)
    if n==2:
        print '>2:',L2[5],'第2步使用天平：天平左右砝码(%d,%d)；'%(L2[2][2],L2[2][3])
        P2(L2[3][0],L2[3][1],L2[3][2],L2[2][0],L2[2][1],L2[2][3])
        P3(hbi,hbx,hby,outALL)
    if n==3:
        print '>3:',L3[5],'第3步使用天平：天平左右砝码(%d,%d)；'%(L3[2][2],L3[2][3])
        P2(L3[3][0],L3[3][1],L3[3][2],L3[2][0],L3[2][1],L3[2][3])
        P3(hbi,hbx,hby,outALL)
def P2(fi,x,y,fhi,fmr_x,fmr):
    if fi == 1:
        print '%d平移为%d和%d'%(x,y,x-y)
    else: 
        print '%d平分为%d和%d'%(x,y,x-y)
    if fhi == 1:  ##fmki
        print '（%dg=%dg砝码+%dg沙堆）'%(fmr,fmr_x,fmr-fmr_x)
def P3(hbi,hbx,hby,outALL):
    if hbi == 1:
        print '-*:',outALL,'\t沙堆合并:%d与%d合并得%d'%(hbx,hby-hbx,hby)
        ##if (hby==50)or(hby==90):print '剩下的合并为%d'%(140-hby)
##*********主程序************

##L0=F(71,69,0,0,1)[:]
##print '*****L0:'
##for i in L0:
##    print i
run=1
if run==1:
    L0=F(140,0,0,0,0)[:]  ##(x1,x2,x3,x4,n)
    for db_L in L0:
        L1=db_L[:] ##;print L1  ##db_L(70,70,0,0,1)
        La=F(db_L[0][0],db_L[0][1],db_L[0][2],db_L[0][3],db_L[1])[:]
        for db_La in La:
            L2=db_La[:] ##;print L2  ##db_L(35,35,70,0,2)
            Lb=F(db_La[0][0],db_La[0][1],db_La[0][2],db_La[0][3],db_La[1])[:]
            L3_last=[]
            for db_Lb in Lb:
                L3=db_Lb[:] ##;print L3 ##db_L(50,15,35,70,3)
                if ((L3[0][0]==50)or(L3[0][0]==90)):  ##(L3[0][0]==50)or
                ##去重
                    L3_now = L3[5][:]
                    L3_now.sort()
                    if L3_now == L3_last:continue
                    L3_last = L3_now
                ##*******判断输出*******
                    print '\n方法%d：'%(shu)
                    print '[140,0,0,0]'
                    shu+=1
                    P1(L1[1], L1[4][0], L1[4][1], L1[4][2], L1[0])
                    P1(L2[1], L2[4][0], L2[4][1], L2[4][2], L2[0])
                    P1(L3[1], L3[4][0], L3[4][1], L3[4][2], L3[0])
                    
