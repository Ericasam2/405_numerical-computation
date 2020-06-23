'投针实验'
import math
import numpy as np
n=100000    #实验次数
a=0.001     #平行线距离
l=0.0003    #针的长度
x_axis=np.zeros(10000)  
def create_table(tb_size,gap):   #生成用来投针的平行线数组
    x_axis[0]=0
    for i in range(0,int(tb_size//gap)):  #用x坐标来代表平行线组
        x_axis[i+1]=x_axis[i]+gap    

def needle():    #投针实验主函数
    count=0
    create_table(1,a)
    for i in range(n):
        theta=np.random.uniform(0,2*3.14159)  #随机生成0~2pi的θ，表示投针落地的角度
        x1=np.random.uniform(0,1)        #随机在（0，1）之间生成x1，表示投针一端落地的坐标
        x2=x1+l*math.cos(theta)          #投针另一端落地的坐标
        for k in range(int(1//a)):
            if((x1-x_axis[k])*(x2-x_axis[k])<0):  #当两端在某一条平行线的两端，计数加一
                count=count+1
    f=count/n                             #计算投针碰到平行线概率 
    print(2*l/(f*a))
    
needle()
        
