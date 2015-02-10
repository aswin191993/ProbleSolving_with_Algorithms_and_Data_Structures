
import re


class stack:
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
			print self.deque


def html(scr):
	oper=re.findall(r'</\?>',scr)
	tag_stack = stack()
	for tag in tagList:
		if tag[0] == '':
			tag_stack.push(tag)
		else:
			if tag_stack.is_empty():
				return False
			else:
				top_tag = tag_stack.pop()
				if top_tag[1] != tag[1]:
					return False
	return True



scr="""
<html>
	<head>
		<title>
			Example
		</title>
	</head>
	<body>
		<h1>Hello, world</h1>
	</body>
</html>




