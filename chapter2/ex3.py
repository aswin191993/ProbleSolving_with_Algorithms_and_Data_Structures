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
#		pop function manuval pgm
#		fl=len(self.items)
#		temp=self.items[fl-1]
#		del self.items[fl-1]
#		print 
		return self.items.pop()

	def peek(self):
		fnl=len(self.items)
		return self.items[fnl-1]


def infix_to_postfix(infix):
        op_stack=stack()
        othr=list(infix)
	for i in othr:
		if i in "0123456789":
			op_stack.push(int(i))
		else:
			op2=op_stack.pop()
			op3=op_stack.pop()
			result=math(str(i),op2,op3)
			op_stack.push(result)

					
	while op_stack.emptstr() == False:
		print op_stack.pop()

def math(op,op1,op2):
	if op == "*":
		return op1*op2
	elif op == "/":
		return op1/op2
	elif op == "+":
		return op1+op2
	elif op == "-":
		return op1-op2

	
		
#c=stack()
#c.push("34")
#c.push("353")	
#print c.pop()
#print c.pop()
infix_to_postfix("34*6+")
#print math("*",4,5)
