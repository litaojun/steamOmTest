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
if __name__ =="__main__":
    a = Decimal('0.01')
    b = float(a)
    print(a )
    print(type(a))
    print(b)
    print( type(b))