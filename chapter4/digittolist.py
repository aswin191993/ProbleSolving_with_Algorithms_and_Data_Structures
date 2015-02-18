
def sumofls(s):
	s.insert(0,s%10)
	if s/10 != 0:
		return	s.split(sumofls(s/10)	
	else:
		return 


s=1234


print sumofls(s)

