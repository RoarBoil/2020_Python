class PrimeNumbers:
	def __init__(self,start,end):         #start为起始位置，end为终止位置
		self.start=start
		self.end=end
	def isPrimeNum(self,k):               #判断是否为素数
		if k<2:
			return False
		for i in range(2,k):
			if k%i==0:
				return False
			return True
	def __iter__(self):                   #从起始到结束不断迭代
		for k in range(self.start,self.end):
			if self.isPrimeNum(k):
				print('数据范围由%d到%d' % (self.start, self.end))           #打印
				yield k
for x in PrimeNumbers(1,500):
		print(x)

