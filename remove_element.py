array = [1,5,2,9,3,2,0,2,1]

elem = 2

def remove_element(arr, elem):
	i = 0
	j = 0

	while(j < len(arr)):
		if not (arr[j] == elem):
			print i
			arr[i] = arr[j]
			i+=1
		j+=1

	return i	





assert remove_element(array, elem) == 6

print "done"