class DisjointSets:


	
	def __init__(self, n):
		self.id = list(range(n))
		self.size = [1] * n

	def get(self):
		return self.id,self.size

	def find(self,x):
		return self.id[x]


	def root(self,i):
		j = i
		while (j!=self.id[j]):
			self.id[j] = self.id[self.id[j]] 
			j = self.id[j]
		return j

	def union(self,p,q):
		i = self.root(p)
		j = self.root(q)
		if (self.size[i]<self.size[j]):
			self.id[i]=j
			self.size[j]=self.size[i]+self.size[j]
		else :
			self.id[j]=i
        	self.size[i]=self.size[i]+self.size[j]

	def connected(self,p,q):
		return self.root(p) == self.root(q) 
			

	def getlength(self):
		return len(self.id)

if __name__ == "__main__":
	d = DisjointSets(10)
	print d.get()
	d.union(0,5)
	d.union(5,6)
	d.union(6,1)
	d.union(3,4)
	print d.get()
	d.union(9,4)
	d.union(8,3)
	d.union(1,2)
	d.union(2,7)
	print d.get()
	print d.connected(1,7)

	