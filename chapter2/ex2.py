class stack:
	def __init__(self):
		self.items=[]

	def __str__(self):
		return "stack" 

	def emptstr(self):
		if self.items == []:
			return True
		else:
			return False

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		fnl=len(self.items)
		return self.items[fnl-1]

	
c=stack()

c.push("asdd")		
c.push("aswin")
c.push("dfgh")

print c.emptstr()

print c.peek()
print c.pop()
print c.pop()
print c.emptstr()
