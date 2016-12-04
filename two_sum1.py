# Simple Two Sum

'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
For example:
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

def two_sum(input_list, target):
	hmap = {}
	
	x=0
	y=0

	for i in xrange(0, len(input_list)):

		if input_list[i] in hmap:
			index = hmap[input_list[i]]
			x = index+1
			y = i + 1

		
		else:
			hmap[target - input_list[i]] = i

	out =  "index1 = {}, index2 = {}".format(x,y)
	return out



input_list = [2, 11, 7, 15]
target = 9

print two_sum(input_list, target)