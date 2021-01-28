"""
O(n) time and O(1) space can be achieved with Boyer–Moore majority vote algorithm.
"""
from collections import Counter


class Solution(object):
    def majorityElement1(self, nums):
        """
        Sorts and returns the middle element of array.
        Middle element will always be the majority element.

        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn) time (tim sort)
        # O(1) space
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        # O(n) space
        num_set = Counter(nums)
        return num_set.most_common(1)[0][0]

    def majorityElement3(self, nums):
        """
        If you insist on using a dict.

        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        # O(n) space
        num_set = dict()
        for x in nums:
            if x in num_set:
                num_set[x] += 1
            else:
                num_set[x] = 1
        return max(num_set, key=num_set.get)
