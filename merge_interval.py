# MERGE Intervals
"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]
"""

def merge_overlapping_intervals(input):
	start = 0
	end = 1
	result = []
	if (input == None or len(input)<=1):
		return input

	# SORT intervals using self custom defined comparator key, inplace
	input.sort(key=lambda x:x[start])
	prev = input[start]
	for i in xrange(1, len(input)):
		curr = input[i]
		if prev[end] >= curr[start]:
			merged = [prev[start], max(prev[end], curr[end])]
			prev = merged
		else:
			result.append(prev)
			prev = curr

	result.append(prev)
	return result



input_array = [[1,3],[2,6],[8,10],[15,18]]
print merge_overlapping_intervals(input_array)