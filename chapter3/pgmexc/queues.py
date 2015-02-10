class queues:
	def __init__(self):
		self.items=[]

	def __str__(self):
		return "queues"

	def is_empty(self):
		if self.items == []:
			return True
		else:
			return False
	
	def enque(self,item):
		self.items.append(item)

	def deque(self):
#		pop function manuval pgm
		fl=len(self.items)
		temp=self.items[0]
		del self.items[0]
		return temp 

	def prnt(self):
		while self.is_empty() != True:
			print self.deque()



q=queues()
q.enque("asd")
#q.enque("uio")
#q.enque("bnnm")
#print q.deque()
#print q.is_empty()
#q.prnt()
