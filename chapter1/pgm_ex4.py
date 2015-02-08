l="6538921"
ls=list(l)


def random(ls,k):
	list_new=ls
	lth=len(ls)
	tenp=0
	for i in range(lth):
		for j in range(lth):
			if ls[i] < ls[j]:
				temp=ls[i]
				ls[i]=ls[j]
				ls[j]=temp
	
	kth=ls[k]			
	print ls
	print "kth:",kth
	 
		

random(ls,3)
