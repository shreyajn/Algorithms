def insertsort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j = i-1
		while j>0 and arr[j]>key:
			arr[j+1]=arr[j]
			j = j-1
		arr[j+1]=key 
	return arr

if __name__ == "__main__":
	arr = [0,1,5,3,7,5,4]
	barr = insertsort(arr)
	print barr