# Search in rotated sorted array, pivot point of rotation unkonwn

# Duplicates are allowed

def search(nums, target):

	left = 0
	right = len(nums) - 1

	while (left <= right):

		mid = (left + right)/2

		if nums[mid] == target:
			return True

		if nums[left] < nums[mid]:
			if nums[left] < target and target <= nums[mid]:
				right  = mid - 1
			else:
				left = mid + 1
		elif nums[left] < nums[mid]:
			if nums[mid] <  target and target < nums[right]:
				left = mid + 1
			else:
				right  = mid - 1
		else: # Handles duplicates, just moves the pointer		
			left +=1
	
	return False