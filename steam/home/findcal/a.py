#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: a.py 
@time: 2018/6/13 16:31 
"""
from decimal import  Decimal
def a():
    a = Decimal('0.01')
    b = float(a)
    print(a )
    print(type(a))
    print(b)
    print( type(b))

def b(num=1):
    fun = lambda x:fun(x-2)+fun(x-1) if x>=3 else 1
    t = fun(num)
    print(t)
    return t
if __name__ =="__main__":
    x = b(2)
    print(x)
    fun = lambda x: fun(x - 2) + fun(x - 1) if x >= 3 else 1
    num = sum([ fun(i) for i in range(1,6)])
    print(num)
