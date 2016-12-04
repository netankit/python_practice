nums = [0,1,0,3,12]

result  = [1,3,12,0, 0]



def remove_zeros(arr):
	i = 0
	j = 0

	while (j < len(arr)):
		if arr[j] == 0:
			j+=1
		else:
			arr[i] = arr[j]
			i+=1
			j+=1
	while(i < len(arr)):
		arr[i] = 0
		i+=1

	print arr
	return arr




assert remove_zeros(nums) == result