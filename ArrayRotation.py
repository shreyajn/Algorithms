
def array_rot(A,d):
	temp = [0]*d
	for i in range(d):
		temp[i] = A[i]
	B = [0]*len(A)
	for i in range(len(A)-d):
		B[i] = A[i+d]
	for i in range(len(A)-d,len(A)):
		B[i] = temp[len(A)-d-i]
	return B

def array_rot2(A,d):
	for i in range(d):
		array_rotonce(A)
	print A

def array_rotonce(A):
	temp = A[0]
	for i in range(len(A)-1):
		A[i] = A[i+1]
	A[i+1] = temp
	
def reverse(A,start,end):
	while(start<end):
		temp = A[start]
		A[start] = A[end]
		A[end] = temp
		end = end-1
		start = start +1

def rot3(A,d):
	n=len(A)
	reverse(A,0,d-1)
	reverse(A,d,n-1)
	reverse(A,0,n-1)
	print A

B=[1,2,3,4,5,6,7]
rot3(B,4)
