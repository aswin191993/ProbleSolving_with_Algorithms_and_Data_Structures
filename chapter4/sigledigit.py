def SingleDigit(s):
	if len(s) == 1:
		return s[0]
	else:
		
		return s[0]*(10**len(s[1:]))+SingleDigit(s[1:])
		


s=[1,2,3,4,5,6,7,8]


print SingleDigit(s)

