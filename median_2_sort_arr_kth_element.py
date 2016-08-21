# Find median of two sorted arrays using the method to find 
# the kth element in two sorted arrays.


def findMedianTwoSortedArrays(arr1, arr2):
	arr1_len = len(arr1)
	arr2_len = len(arr2)

	# Check based on sum lengths if the median element is odd or even

	if not ((arr1_len + arr2_len) %2 == 0): # ODD
		return findKthElement(arr1, arr2, (arr1_len + arr2_len)/2, 0, arr1_len-1, 0, arr2_len - 1)
	else:
		return (findKthElement(arr1, arr2, (arr1_len + arr2_len)/2, 0, arr1_len-1, 0, arr2_len - 1) +
		findKthElement(arr1, arr2, ((arr1_len + arr2_len)/2)-1, 0, arr1_len-1, 0, arr2_len - 1)) * 0.5


def findKthElement(arr1, arr2, k, start_arr1, end_arr1, start_arr2, end_arr2):
	len_arr1 = end_arr1 - start_arr1 + 1
	len_arr2 = end_arr2 - start_arr2 + 1

	# Special cases
	if len_arr1 == 0:
		return 	arr2[start_arr2 + k]

	if len_arr2 == 0:
		return 	arr1[start_arr1 + k]

	if k == 0:
		return arr1[start_arr1] if arr1[start_arr1] < arr2[start_arr2] else arr2[start_arr2]


	mid_arr1 = len_arr1	* k / (len_arr1 + len_arr2) # A's middle count
	mid_arr2 = k - mid_arr1 - 1						# B's middle count

	# Array indexes
	mid_arr1 = mid_arr1 + start_arr1
	mid_arr2 = mid_arr2 + start_arr2

	if arr1[mid_arr1] > arr2[mid_arr2]:
		k = k - (mid_arr2 - start_arr2 + 1)
		end_arr1 = mid_arr1
		start_arr2 = mid_arr2 + 1
	else:
		k = k - (mid_arr1 - start_arr1 + 1)
		end_arr2 = mid_arr2
		start_arr1 = mid_arr1 + 1

	return findKthElement(arr1, arr2, k, start_arr1, end_arr1, start_arr2, end_arr2)

# Test
arr1 = [1,2,3,4,5,6,7]
arr2 = [9,10,11,12,13,14]

print findMedianTwoSortedArrays(arr1, arr2)

# Test
arr1 = [1,2,3,4,5,6]
arr2 = [9,10,11,12,13,14]

print findMedianTwoSortedArrays(arr1, arr2)