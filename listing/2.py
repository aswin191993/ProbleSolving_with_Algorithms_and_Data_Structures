class fraction:
	def __init__(self,re,img):
		self.r = re
		self.i = img
	
	def __str__(self):
		return "divisible:"+str(self.r)+"/"+str(self.i)

	def gdc(self):
		while((self.r)%(self.i) != 0):
			odre = self.r
			odimg = self.i
			
			self.r = self.i
			self.i = odre%odi
				
		return "gdc:"+str(self.i)

	
#	gdc(self)


c=fraction(20,10)
print c
print c.gdc()
