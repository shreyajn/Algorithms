class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printlist(self):
		temp=self.head
		while(temp):
			print temp.data
			temp = temp.next

	def insert_head(self,new_data):
	
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def delete(self,key):
		temp = self.head
		while(temp!= None and temp.data==key):
			self.head = temp.next
			temp = None
		
		while(temp!= None and temp.data!=key):
			prev = temp
			temp = temp.next 
				
		if (temp == None):
			return

		prev.next = temp.next 
		temp = None
		temp = prev.next

	def insert_middle(self,prev,new_data):
		new_node = Node(new_data)
		temp = self.head
		while(temp):
			if (temp == prev):
				new_node.next = prev.next
				prev.next = new_node
			temp = temp.next

	def insert_end(self,new_data):
		new_node = Node(new_data)
		if (self.head == None):
			self.head = new_node
			return
		temp = self.head
		while(temp.next!=None):
			temp = temp.next
		temp.next = new_node

	def count(self):
		count = 0 
		temp = self.head
		while (temp):
			count+=1
			temp = temp.next
		print count

	def delete_pos(self,position):
		temp = self.head
		prev = temp
		while (temp!=None):
			if (position==1):
				temp = self.head
				self.head = temp.next
				temp = None
			else:
				for i in range(position-1):
					prev = temp
					temp = temp.next
				prev.next = temp.next
				temp = None

	def search(self,x):
		temp = self.head
		while(temp!=None):
			if(temp.data==x):
				return True
			temp = temp.next

	def reverse(self):
		first = None
		second = self.head
		while(second is not None):
			third = second.next
			second.next = first
			first = second 
			second = third
		self.head = first 

	

if __name__ == '__main__':

	ll = LinkedList()
	ll.head = Node(1)
	second = Node(2)
	third = Node(3)
	ll.head.next = second
	second.next = third
	ll.insert_head(5)
	ll.insert_middle(second,4)
	ll.insert_end(6)
	ll.insert_end(7)
	ll.insert_middle(second,8)
	ll.insert_head(9)
	ll.delete_pos(2)
	ll.printlist
	ll.reverse()
	ll.printlist()
	
	
	



