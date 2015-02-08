class stack:
	def __init__(self,items):
		self.item=items

	def __str__(self):
		return "print reverse" 

	def rev_string(self):
		self.item=list(self.item)
		lst2=[]
		for i in range(len(self.item)):
			j=i+1
			lst2.append(self.item[-j])
		
		self.item=lst2
		return self.item

	
c=stack("asdfgh")
print c		
print c.rev_string()
