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

	def insert(self,j,item):
		return self.items.insert(j,item)

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


def infix_to_postfix(infix_expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	op_stack = stack()
	postfix_list = []
	token_list = list(infix_expr)
	j=1
	for token in token_list:
		
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			op_stack.push(token)
		else:
			postfix_list.append(token)

	for sign in postfix_list:

		if sign in "/*":
			temp=op_stack.peek()
			if temp in "-+":
				op_stack.insert(j,sign)
			else:
				j=j+1
				op_stack.insert(j,sign)
		else:
			j=j+1
			op_stack.insert(j,sign)
				
						
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
infix_to_postfix("A+B*C+D")
#print math("*",4,5)
