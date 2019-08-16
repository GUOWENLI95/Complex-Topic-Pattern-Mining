import numpy

#算法三所用的数据结构
'''
#time interval list,之前session按5小时切分，则此处最大时间间隔是5小时
此处时间间隔是一个超参数
'''

aHour=3600
# TI=[int(aHour*1),int(aHour*2),int(aHour*3),int(aHour*4),int(aHour*6),int(aHour*9)]
# TI=[int(aHour*0.25),int(aHour*0.5),int(aHour*1),int(aHour*2),int(aHour*3)]

# TI=[aHour*1,aHour*3,aHour*6,aHour*9,aHour*12,aHour*24]
TI=[aHour*1,aHour*3,aHour*6]
# TI=[aHour*24]
# TI=[2,3,4,5,6,7,100]


class Prefix:
    def __init__(self,tau,i,j,k,p):
        self.sessID = i
        self.tau=tau
        self.next_pos=j
        self.pos=k
        self.prob=p



class Temp:
    def __init__(self,i,tau,pos,prob,time,oriProb):
        self.sessID=i
        self.tau=tau
        self.pos=pos
        self.prob=prob
        self.time=time
        self.oriProb=oriProb



class STP_Supp:
    def __init__(self,ldaStr,tau,prob_list,supp,l,contain):
        self.ldaStr=ldaStr
        self.tau=tau
        self.prob_list=prob_list
        self.supp=supp
        self.len=l
        self.contain=contain

if __name__=="__main__":
    t1=Temp(i=1, tau=0, pos=10, prob=.1, time=1, oriProb=None)
    t2=Temp(i=1, tau=0, pos=9, prob=.1, time=1, oriProb=None)
    T=[t1,t2]
    x=max(T,key=lambda i:i.pos)
    print(x.pos)