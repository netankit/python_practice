"""
Problem:
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c) The solution set must not contain duplicate triplets.
For example, given array S = {-1 0 1 2 -1 -4},
   A solution set is:
   (-1, 0, 1)
   (-1, -1, 2)
"""
def threeSum(input_list):
	result = []

	if input_list == None or len(input_list) == 0:
		return result

	input_list.sort()


	for i in xrange(0, len(input_list)-2):
		if i ==0 or input_list[i] > input_list[i-1]:
			j = i + 1
			k = len(input_list) - 1

			while (j < k):
				if input_list[i] + input_list[j] + input_list[k] == 0:
					l = []
					l.append(input_list[i])
					l.append(input_list[j])
					l.append(input_list[k])
					result.append(l)

					j += 1
					k -= 1
					# Duplicates	
					while (j < k and input_list[j] == input_list[j-1]):
						j+=1
					while (j < k and input_list[k] == input_list[k+1]):
						k-=1

				elif input_list[i] + input_list[j] + input_list [k] < 0:
					j+=1
				else:
					k-=1


	return result

print threeSum([-1 ,0 ,1, 2, -1, -4, 3, 4, 2, -1])