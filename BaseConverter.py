class Stack:
	def __init__(self):
		self.stack = []
		
	def isEmpty(self):
		if len(self.stack)==0:
			return "Stack is empty"
	def push(self,x):
		self.stack.append(x)
	def pop(self):
		if len(self.stack)!=0:
			item = self.stack.pop()
			return item
def BaseConv(n,base):
	digits = "0123456789ABCDEF"
	s = Stack()
	while n>0 :
		r= n%base
		s.push(r)
		n = n//base
	s.printit()
	bin=""
	while not(s.isEmpty()):
		bin += digits[s.pop()]
	print bin
BaseConv(25,16)
