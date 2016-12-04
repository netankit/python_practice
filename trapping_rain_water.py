# Trapping Rain water problem.

input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6


def trap(height):
	result = 0
	
	if height == None  or len(height) < 2:
		return result

	left = [0] * len(height)
	right = [0] * len(height)

	# Scan from Left to Right
	maximum = height[0]
	left[0] = height[0]
	
	for i in range(1, len(height), 1):
		if height[i] < maximum:
			left[i]  = maximum
		else:
			left[i] = height[i]
			maximum = height[i]

	# Scan Right to Left.
	maximum = height[len(height) - 1]
	right[len(height) - 1] = height[len(height) - 1]
	for i in range(len(height) - 2, -1, -1):
		if height[i] < maximum:
			right[i] = maximum
		else:
			right[i] = height[i]
			maximum = height[i]


	# Total
	for i in xrange(0, len(height), 1):
		print result
		result += min(left[i], right[i]-height[i])

	print "out:"
	print result	
	return result


assert trap(input) == output 