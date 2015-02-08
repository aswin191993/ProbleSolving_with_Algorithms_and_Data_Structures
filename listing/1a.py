class fraction:
	def __init__(self,re,img):
		self.r = re
		self.i = img
	
	def __str__(self):
		return str(self.r)+"/"+str(self.i)


c=fraction(5,7)
print c
