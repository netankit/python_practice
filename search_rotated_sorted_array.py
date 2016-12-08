# Search in rotated sorted array, pivot point of rotation unkonwn

# No Duplicates
# Only in this case the binary search method works. 
# once duplicated are introcuced then revert to looping through the list and the checking for target.

def binary_search( nums, left, right, target):

	if left > right:
		return -1

	mid = (left + right) / 2 # or, left + (right - left)/2 --> Easier to compute 

	if target == nums[mid]:
		return mid

	if nums[left] <= nums[mid]:
		if nums[left] < target and target <= nums[mid]:
			return binary_search(nums, left, mid -1, target)
		else:
			return binary_search(nums, mid + 1, right, target)
	else:
		if nums[mid] < target and target <= nums[right]:
			return binary_search(nums, mid+1, right, target)
		else:
			return binary_search(nums, left, mid-1 , target)
		
def search_no_duplicates(nums, target):
	return binary_search(nums, 0, len(nums) - 1, target)
