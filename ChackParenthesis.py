
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
			self.stack.pop()

	def printit(self):
		print self.stack

def checkpar(s):
	st = Stack()
	balanced = True
	i=0
	while balanced and i<len(s):
		sym = s[i]
		if sym =='(':
			st.push(sym)
		else:
			if st.isEmpty():
				balanced = False
			else:
				st.pop()
		i = i+1
	if balanced and st.isEmpty():
		return True
	else:
		return False

print checkpar('(())()((()))')
