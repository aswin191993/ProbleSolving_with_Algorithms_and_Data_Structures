
class fraction:
	def __init__(self,re,img):
		self.r = re
		self.i = img
	
	def __str__(self):
		return "divisible:"+str(self.r)+"/"+str(self.i)

	def __sub__(self,other):
                common=1
                newnum = self.r*other.i - self.i*other.r
                newd = self.i * other.i
                common=gdc(newnum,newd)
                nr = newnum / common
                nimg = newd / common
                return "SUB:"+str(nr)+"/"+str(nimg)

	def __mul__(self,other):
                common=1
                newnum = self.r*other.r
                newd = self.i * other.i
                common=gdc(newnum,newd)
                nr = newnum / common
                nimg = newd / common
                return "MUL:"+str(nr)+"/"+str(nimg)

	def __div__(self,other):
                common=1
                newnum = self.r*other.i
                newd = self.i * other.r
                common=gdc(newnum,newd)
                nr = newnum / common
                nimg = newd / common
                return "DIV:"+str(nr)+"/"+str(nimg)

def gdc(fr,fimg):
	while((fr)%(fimg) != 0):
		odre = fr
		odimg = fimg
		
		fr = fimg
		fimg = odre%odimg
			
	return fimg

	
#	gdc(self)


c=fraction(12,5)
d=fraction(6,3)
print c
#print c.gdc()
print d
print c-d
print c*d
print c/d
