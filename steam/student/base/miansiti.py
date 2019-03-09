#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: miansiti.py 
@time: 2018/12/15 23:20 
"""

#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
def a1():
	tls =[[1,2],[3,4],[5,6]]
	print([b for a in tls for b in a])

def func():
	pass


if __name__ == "__main__":
	a1()