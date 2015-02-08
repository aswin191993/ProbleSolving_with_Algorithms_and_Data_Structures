
class fraction:
	def __init__(self,re,img):
		self.r = re
		self.i = img
	
	def __str__(self):
		return "divisible:"+str(self.r)+"/"+str(self.i)

	def __sub__(self,other):
                common=1
                newnum = self.re*other.img - self.img*other.re
                newd = self.img * other.img
                common=gdc(newnum,newd)
                nr = newnum / common
                nimg = newd / common
                return "SUB:"+str(nr)+"/"+str(nimg)

	def __mul__(self,other):
                common=1
                newnum = self.re*other.re
                newd = self.img * other.img
                common=gdc(newnum,newd)
                nr = newnum / common
                nimg = newd / common
                return "MUL:"+str(nr)+"/"+str(nimg)

	def __div__(self,other):
                common=1
                newnum = self.re*other.img
                newd = self.img * other.re
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


d=fraction(4,3)
print d
