k="asdfghjkl"
def xepop(k):
	lst=list(k)
	print lst.pop()
	print lst.pop(0)
	lst.append('m')
	print lst	
	print set(k)
	if lst[2] in lst:
		print lst[2]

	

	
xepop(k)

