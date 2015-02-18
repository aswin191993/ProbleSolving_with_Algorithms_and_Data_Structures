
def tree(r):
	return [r,[],[]]

def last(root,lval):
	if root[1] == []:
		root.pop(1)
		return root.insert(1,[lval,[],[]])
		
	else:
		ne=root[1]
		return last(ne,lval)
k=tree(4)
#k=[2,[3,[4,[],[]],[]],[]]
#print k
last(k,5)
#print k
last(k,7)
print k
#print k
#in_left(k,9)
#print k
#in_left(k,12)
#print k
#in_right(k,20)
#print k
