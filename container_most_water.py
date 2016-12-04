# Container with most water.
import random
height_arr = [random.randrange(0,50) for _ in range(0,8)]

print "Input: {}".format(height_arr)

def maxArea(height):
	
	if height == None or len(height) < 2:
		return 0

	maximum = 0
	left = 0
	right = len(height) - 1

	while(left < right):
		maximum = max(maximum, (right-left) * min(height[left], height[right]))

		if height[left] < height[right]:
			left += 1
		else:
			right += 1
	return maximum

print "Output: {}".format(maxArea(height_arr))