def SumOfDigits(s):
	if len(s) == 1:
		return s[0]
	else:
		return s[0]+sumofls(s[1:])




s=[1,2,3,4,5,6]


print sumofls(s)

