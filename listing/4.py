class fraction:
	def __init__(self,num):
		self.n = num
	
	def __str__(self):
		return str(self.n)

	def __gt__(self,othr):
                if self.n > othr.n:
                	return True
		else:
			return False
	def __ge__(self,othr):
                if self.n >= othr.n:
                        return True
                else:
                        return False
	
	def __lt__(self,othr):
                if self.n < othr.n:
                        return True
                else:
                        return False

	def __le__(self,othr):
                if self.n <= othr.n:
                        return True
                else:
                        return False

c=fraction(7)
d=fraction(6)
print c
print d
print "gt",c>d
print "ge",c>=d
print "lt",c<d
print "le",c<=d
