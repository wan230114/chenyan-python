#!/usr/bin/python
# -*- coding: cp936 -*-

shu = 1     ##��ǰ�ҳ��ķ���

print '��ƽ���γ���:'
print '  ��һ����ƽ,2�˺�7�������һ��,'
print '  ��������ƽ���뽫140���ηֳ�50,90������,'
print '  �涨ֻ��ʹ��3����ƽ���г���������Щ������'

##*******ȷ����ƽ��fml��fmr*******
def F(x1,x2,x3,x4,nn):
    A = [0,2,7,9]
    B = [0,2,7,9]
    cpL = []
    dbALL=[x1,x2,x3,x4]
    n=nn    ##��ǰѭ���Ѿ��������˵�n��
    for dbA in A:
##        print '��1��for dbA in A:'
        ALL = dbALL[:]
    ##    ȷ��fml
        fml = dbA
    ##    ȷ��fmr������
        if fml==0: B = [0,2,7,9]
        if fml==2: B = [0,7]
        if fml==7: B = [0,2]
        if fml==9: B = [0]
    ##    ȷ��fmr
        for dbB in B:
##            print '��2��for dbB in B:'
            f1_ALL = ALL[:]  ##;print f1_ALL
            FMR=[]
            FMR.append([dbB,0])
            n_fmr=1
            while n_fmr <= n: 
                if f1_ALL[n_fmr]>0:
                    dbB_x=dbB+f1_ALL[n_fmr] ##;print dbB,dbB_x
                    FMR.append([dbB_x,1]) ##�����б�洢�ϲ�ָ�ꡰ1��
                n_fmr+=1
            for db_FMR in FMR:
##                print '��3��while n_FMR<len(FMR):'
                f2_ALL = f1_ALL[:]
                fmr = db_FMR[0]
                fmki= db_FMR[1]   ##����ɳ��������ϲ�����ָ��,������ƺ��ڿ�ȥ���Ż�
    ##*******�������*******
                x = f2_ALL[0]
                y = 0   ##;print 'fm:',fml,fmr,fmki
                Y=[]
                if fml < fmr:
                    y = x-(fmr-fml)
                    Y.append([y,1])     ##������1ƽ�ƣ�2ƽ�֣�y:���y(x)
                if fmki==0:             ##�ϲ���ɳ��������Ĳ��ܲ���ƽ��
                    y = (x+fmr+fml)*0.5-fml;
                    if int(y)==y:
                        y=int(y)
                    Y.append([y,2])
    ##*******��¼����*******
                for db_Y in Y:
##                    print '��4��for db_Y in Y:'
                    f3_ALL=f2_ALL[:]
                    if db_Y[0]<=0:
                        continue ##yֵ������ʱ������һ��ѭ��
                    f3_ALL[0] = db_Y[0]
                    n_next = n
##                    print 'n',n,'',f3_ALL
                    while n_next>0:
                        f3_ALL[n_next+1] = f3_ALL[n_next]
                        n_next = n_next - 1
                    f3_ALL[1] = x - f3_ALL[0]
    ##*******ɳ�Ѻϲ�����*******
                    HB=[[f3_ALL[0],0,0,0]]  ##HB=[�ϲ���y��1�����Ѿ��ϲ����ϲ�ǰx���ϲ��ĵڼ�����ָ��]
                    if n>=1:
                        n_hb = 1            ##�ϲ��ĵڼ�����ָ��
                        while n_hb <= 3:    ##Y[n_result]##Ϊ����n�������Ľ���׼��
                            if f3_ALL[n_hb]<=0:n_hb+=1;continue;
                            hb=f3_ALL[0] + f3_ALL[n_hb];
                            HB.append([ hb , 1 , f3_ALL[n_hb] , n_hb ])
                            n_hb += 1  ##; if hb==109: print HB
                    for db_HB in HB:
##                        print '��5��for db_HB in HB:'
                        f4_ALL=f3_ALL[:]  ##;print '1',f4_ALL[0],'2',db_HB[0]
                        f4_ALL[0]=db_HB[0]
                        if db_HB[1]==1:
                            f4_ALL[db_HB[3]]=0
                        ##���ˣ���ɵ�n��
                        db_L = [f4_ALL[:]]
                        db_L.extend((n+1, [fmki, dbB, fml , fmr], [db_Y[1], x  , db_Y[0]], [db_HB[1],f3_ALL[0],f4_ALL[0]],f3_ALL))
                        cpL.append(db_L)
    return cpL

##��ӡ����������
def P1(n,hbi,hbx,hby,outALL):
    if n==1:
        print '>1:',L1[5],'��1��ʹ����ƽ��������ƽ(%d,%d)��'%(L1[2][2],L1[2][3])
        P2(L1[3][0],L1[3][1],L1[3][2],L1[2][0],L1[2][1],L1[2][3])
        P3(hbi,hbx,hby,outALL)
    if n==2:
        print '>2:',L2[5],'��2��ʹ����ƽ��������ƽ(%d,%d)��'%(L2[2][2],L2[2][3])
        P2(L2[3][0],L2[3][1],L2[3][2],L2[2][0],L2[2][1],L2[2][3])
        P3(hbi,hbx,hby,outALL)
    if n==3:
        print '>3:',L3[5],'��3��ʹ����ƽ��������ƽ(%d,%d)��'%(L3[2][2],L3[2][3])
        P2(L3[3][0],L3[3][1],L3[3][2],L3[2][0],L3[2][1],L3[2][3])
        P3(hbi,hbx,hby,outALL)
def P2(fi,x,y,fhi,fmr_x,fmr):
    if fi == 1:
        print '%dƽ��Ϊ%d��%d'%(x,y,x-y)
    else: 
        print '%dƽ��Ϊ%d��%d'%(x,y,x-y)
    if fhi == 1:  ##fmki
        print '��%dg=%dg����+%dgɳ�ѣ�'%(fmr,fmr_x,fmr-fmr_x)
def P3(hbi,hbx,hby,outALL):
    if hbi == 1:
        print '-*:',outALL,'\tɳ�Ѻϲ�:%d��%d�ϲ���%d'%(hbx,hby-hbx,hby)
        if (hby==50)or(hby==90):print 'ʣ�µĺϲ�Ϊ%d'%(140-hby)
##*********������************

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
                ##ȥ��
                    L3_now = L3[5][:]
                    L3_now.sort()
                    if L3_now == L3_last:continue
                    L3_last = L3_now
                ##*******�ж����*******
                    print '\n����%d��'%(shu)
                    print '[140,0,0,0]'
                    shu+=1
                    P1(L1[1], L1[4][0], L1[4][1], L1[4][2], L1[0])
                    P1(L2[1], L2[4][0], L2[4][1], L2[4][2], L2[0])
                    P1(L3[1], L3[4][0], L3[4][1], L3[4][2], L3[0])
