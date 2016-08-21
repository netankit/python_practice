# MERGE Intervals
"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]
"""

class Interval(object):
	def __init__(self):
		self.start = 0
		self.end = 0

	def __init__(self, s, e):
		self.start = s
		self.end = e


	




def merge_overlapping_intervals(input):







input_array = [[1,3],[2,6],[8,10],[15,18]]
print merge_overlapping_intervals(input_array)