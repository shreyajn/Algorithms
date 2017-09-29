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

	def printit(self):
		print self.stack

def DectoBin(n):
	s = Stack()
	while n>0 :
		r= n%2
		s.push(r)
		n = n//2
	s.printit()
	bin=""
	while not(s.isEmpty()):
		bin += str(s.pop())
	print bin
DectoBin(42)

