#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: listfun.py 
@time: 2018/12/9 10:36 
"""
from functools import cmp_to_key

def cmpfuna(a,b):
	"""
	https://www.cnblogs.com/cnhkzyy/p/8678996.html
	python3.x中取消了cmp参数，也不支持直接往sort()里面传函数，但可以构造排序函数传递给key来实现
	其中的规律就是：两两比较，如果返回为正，则交换两者的位置，即y在前x在后，
	否则x在前y在后。也可以这样解释，升序就是拿第一个数比对后面的数，降序就是拿最后一个数比对前面的数。
	:param a:
	:param b:
	:return:
	"""
	if a > 0 and b > 0:
		return a - b
	elif a>0 and b<0:
		return -1
	elif a<0 and b>0:
		return 1
	elif a<0 and b<0:
		return b - a
def cmpfunb(a,b):
	return b-a

def testListSort():
	alst = [3, 33, -2,2,-1, 9,-5, 25,-6,-31,-23, 3, 9, 90, 1, 5, 89]
	print(alst)
	# alst.sort(key = lambda a:a)
	# print(alst)
	# alst.sort(key = cmp_to_key(cmpfuna))
	alst.sort(key = cmp_to_key(lambda a,b:a-b if a>0 and b>0  -1 else b-a ))
	print(alst)
	alsta = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	print(alsta[0::2])
	print(alsta[-1:0:-2])
	mystring = "litaojun"
	print(mystring[-1::-2])

def sortListA():
	data = ['-', '-', '+', '+', '+', '-', '+', '-', '+', '-', '-']
	def ast(a = []):
		for i in range(len(data)):
			if a[i] == "-":
				for j in range(len(data)-1,0,-1):
					if i<j:
						if a[j] == "+":
							a[i],a[j] = a[j],a[i]
					else:
						return
	ast(data)
	print(data)

def sortListB():
	data = ['-', '-', '+', '+', '+', '-', '+', '-', '+', '-', '-']
	leftNum = 0
	rigthNum = len(data) - 1
	while rigthNum - leftNum > 0:
		if data[leftNum] == "-" and data[rigthNum] == "+":
			data[leftNum] , data[rigthNum] = data[rigthNum] , data[leftNum]
		elif data[leftNum] == "+":
			leftNum+=1
		elif data[rigthNum] == "-":
			rigthNum-=1
	print(data)


def delListMul():
	als = [1,2,3,1,3,4,5,3,1,3,9,3,21,83,19,8,7,9,6,8]
	print(als)
	num = len(als)
	als.sort()
	n = als[0]
	for i in range(1,num):
		while(i<num and n == als[i]):
			del als[i]
			num -= 1
		if i < num:
			n = als[i]
		else:
			break
	print(als)

def delListMula():
	als = [1,2,3,1,3,4,5,3,1,3,9,3,21,83,19,8,7,9,6,8]
	print(als)
	num = lnum = len(als)
	als.sort()
	n = als[-1]
	i = -2
	while(1):
		if i >= 0-num and n == als[i]:
			del als[i]
			num-=1
		elif i>0-num :
			n = als[i]
			i -= 1
		else:
			break
	print(als)





if __name__ == "__main__":
	#testListSort()
	#sortListA()
	sortListB()
	print("a" or "b")
	print("" or "b")
	print("a" and "b")
	print("a" and "")
	print("a" or "b")
	delListMula()
