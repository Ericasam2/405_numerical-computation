# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:31:25 2020

@author: samgao1999
"""

#牛顿法求根
def newton():
    import math as m
    import numpy as np
    
    def f(x):
        return x**3-3*x-1
    
    def df(x):
        return 3*x**2-3

    n=10              #迭代次数
    x=np.zeros(100)
    x[0]=2              #选定初始近似值（不要选到驻点）
    
    for i in range(n):
        result_f=f(x[i])
        result_df=df(x[i])
        print("f{0}={1:f}".format(i,result_f))
        print("fd{0}={1:f}".format(i,result_df))
        print("x{0}={1:f}".format(i,x))
        print("==============")
    x[i+1]=x[i]-result_f/(result_df+0.0)



#弦截法求根
def newton_scant():
    n=5
    x0=2
    x1=1.9
    x=x0
    y=x1
    def f(x):
        return x**3-3*x-1
    
    for i in range(n):
        print("x{0}={1}".format(i,x))
        print("x{0}={1}".format(i+1,y))
        print("==============")
        temp=y
        y=y-f(y)*(y-x)/(f(y)-f(x))
        x=temp



#二分法求根
def binary():
    import math as m
    n=100                   #迭代次数
    min=m.pi/2+0.01         #设定求根的估值区域
    max=3*m.pi/2-0.01
    x1=min
    x2=max
    
    #设定要求根的函数
    def f(x):
        return x-m.tan(x)
    
    for i in range(n):
        if(f(x1)*f(x2)<0):
            mid=(x1+x2)/2    
            if(f(mid)*f(x1)>0):    #判断二分法的上下区间是不是再零点的两侧
                x1=mid
            else:
                x2=mid
        print("max={0:f},min={1:f}".format(x1,x2))


#牛顿下山法
def newton_down_hill():
    import math as m
    n=100      #迭代次数
    x0=4       
    x=x0
    
    def f(x):
        return x-m.tan(x)
    
    def df(x):
        return 1-1/(m.cos(x))**2
    
    for i in range(n):
        temp=x-f(x)/df(x)
        j=1
        while(abs(f(temp))>abs(f(x))):  #控制牛顿法的单调性
            temp=x-2**(-j)*f(x)/df(x)   #加快收敛速度
            j=j+1
        x=temp
        print("x{0}={1:f}".format(i,x))
        print("==============")


newton_down_hill()