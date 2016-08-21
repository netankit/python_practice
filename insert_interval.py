# Insert and Merge Interval in a list of sorted intervals.

"""
Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
    [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""

def insert_merge_interval(input_list, new_interval):
	start = 0
	end = 1
	
	# If the Existing list provided is non or zie is zero just return the new interval 
	if len(input_list) == 0 or input_list == None:
		if not new_interval is None and len(new_interval) > 0:
			return new_interval
		else:
			return input_list

	result = []

	for i in xrange(0, len(input_list)):
		interval = input_list[i]

		if interval[end] < new_interval[start]:
			result.append(interval)
		elif interval[start] > new_interval[end]:
			result.append(new_interval)
			new_interval = interval
		elif (interval[end] >= new_interval[start]) or  (interval[start] <= new_interval[end]):
			new_interval = [min(interval[start], new_interval[start]), max(new_interval[end], interval[end])]

	result.append(new_interval)		



	return result


# Test Case 1
new_interval = [2,5]
input_list = [[1,3], [6,9]]
print insert_merge_interval(input_list, new_interval)

# Test Case 2
new_interval = [4,9]
input_list = [[1,2],[3,5],[6,7],[8,10],[12,16]]
print insert_merge_interval(input_list, new_interval)
