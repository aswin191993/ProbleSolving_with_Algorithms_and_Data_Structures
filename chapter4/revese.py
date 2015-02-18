def reverse(l):
	if len(l) == 0: 
		return []
	else:
		return [l[-1]] + reverse(l[:-1])
		


s=[1,2,3,4,5,6,7,8]


print reverse(s)
