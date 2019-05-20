#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
def a1():
	tls =[[1,2],[3,4],[5,6]]
	print([b for a in tls for b in a])

def func():
	pass


if __name__ == "__main__":
	a1()