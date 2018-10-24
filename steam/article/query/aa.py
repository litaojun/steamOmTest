#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: aa.py 
@time: 2018/10/23 15:45 
"""

if __name__=="__main__":
    import yaml
    #with open("d:\\tlc.yml") as f:
    with open("d:\\tlc.yml",encoding="utf-8") as f:
        x = yaml.load(f)
        print(x)