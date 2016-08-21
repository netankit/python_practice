# rotate array
rot = [5,6,7,1,2,3,4]

n=7
k=3

arr = [1,2,3,4,5,6,7]

def rot_arr(l, k):
	if l == None or len(l) == 0 or k <0:
		raise Exception('Illegal Input Arguments')
	
	if k > len(l):
		k = k % len(l)

	# first part 
	a = len(l) - k
	reverse(l, 0, a-1)
	reverse(l, a, len(l)-1)
	reverse(l, 0, len(l)-1)
	return l


def reverse(arr, left , right):
	if arr == None or len(arr)==1:
		return

	while(left<right):
		tmp = arr[left]
		arr[left] = arr[right]
		arr[right] = tmp
		left+=1
		right-=1


assert rot == rot_arr(arr, k)