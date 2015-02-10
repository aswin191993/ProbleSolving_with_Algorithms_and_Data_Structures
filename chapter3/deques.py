
class deques:
	def __init__(self):
		self.items=[]

	def __str__(self):
		return "queues"

	def is_empty(self):
		if self.items == []:
			return True
		else:
			return False
	
	def add_rear(self,item):
		self.items.append(item)

	def remove_front(self):
#		pop function manuval pgm
		temp=self.items[0]
		del self.items[0]
		return temp 

	def add_front(self,item):
		self.items.insert(0,item)
		
	def remove_rear(self):
		fl=len(self.items)
                temp=self.items[fl-1]
                del self.items[fl-1]
                return temp

	def prnt(self):
		while self.is_empty() != True:
			print self.remove_front()



#||input test||
#q=deques()
#q.add_rear("asd1")
#q.add_rear("asd2")
#q.add_rear("asd3")
#q.add_front("asd4")
#q.add_front("asd5")
#print q.remove_front()
#print q.remove_rear()
#print q.is_empty()
