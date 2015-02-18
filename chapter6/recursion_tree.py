
def tree(r):
	return [r,[],[]]

def in_left(root,lval):
	if root[1] == []:
		root.pop(1)
		return root.insert(1,[lval,[],[]])
		
	else:
		ne=root[1]
		return in_left(ne,lval)

	
def in_right(root,rval):
	if root[2] == []:
		root.pop(2)
		return root.insert(2,[rval,[],[]])
		
	else:
		new=root[2]
		return in_right(new,rval)




k=tree(4)

print k
in_left(k,5)
print k
in_left(k,7)
in_right(k,6)
print k
in_left(k,9)
print k
#in_left(k,12)
#print k
in_right(k,20)
#print k
in_right(k,21)
in_right(k,22)
print k
