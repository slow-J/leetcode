class Solution(object):
    # Done 2 ways.
    def search_pythonic(self, nums, target, return_index=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return nums.index(target) if target in nums else -1

    def binary_search(self, nums, target, return_index=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid_index = len(nums) // 2
        if nums[mid_index] == target:
            return return_index + mid_index
        elif mid_index == 0:
            return -1
        elif nums[mid_index] > target:
            return self.search(nums[:mid_index], target, return_index)
        else:
            return self.search(nums[mid_index:], target, mid_index + return_index)
