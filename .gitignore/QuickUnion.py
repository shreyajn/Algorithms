class DisjointSets:

	disjoint_set = list()
	
	def __init__(self, n):
		self.disjoint_set = []
		for i in range(n):
			self.disjoint_set.append(i)

	def get(self):
		
		return self.disjoint_set

	def find(self,x):
		return self.disjoint_set[x]


	def root(self,elem):
		while (elem!=self.disjoint_set[elem]):
			elem = self.disjoint_set[elem] 
		return elem

	def union(self,p,q):
		i = self.root(p)
		j = self.root(q)
		self.disjoint_set[i]=j
		return self.disjoint_set

	def connected(self,p,q):
		return self.root(p) == self.root(q) 
			

	def getlength(self):
		return len(self.disjoint_set)

if __name__ == "__main__":
	d = DisjointSets(10)
	print d.get()
	print d.union(0,5)
	print d.union(5,6)
	print d.union(6,1)
	print d.union(3,4)
	print d.union(9,4)
	print d.union(8,3)
	print d.union(1,2)
	print d.union(2,7)
	print d.connected(1,2)

	