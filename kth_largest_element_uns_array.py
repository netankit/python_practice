import heapq


def kthlargestElementUnsortedArray(arr, k):
	arr = [x * -1 for x in arr]
	heapq.heapify(arr)
	for i in xrange(0, len(arr)):
		print arr
		if i+1 == k :
		    return heapq.heappop(arr) * -1
		heapq.heappop(arr) * - 1



test = [3,2,1,5,6,4]
test_k = 4

print kthlargestElementUnsortedArray(test, test_k)