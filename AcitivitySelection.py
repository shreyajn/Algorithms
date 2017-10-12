def maxactivity(s,f):
	n = len(f)
	print "The following activities are selected"
	i=0
	print i,
	for j in range(n):
		if s[j]>=f[i]:
			print j,
			i=j



def maxactivity1(s,f):
	new_s = [s for _,s in sorted(zip(f,s))]
	f.sort()
	print f
	print new_s
	n = len(f)
	print "The following activities are selected"
	i=0
	print i,
	for j in range(n):
		if new_s[j]>=f[i]:
			print j,
			i=j
			
s=[8,5,5,3,4,0]
f=[9,9,7,4,5,2]
maxactivity1(s,f)
