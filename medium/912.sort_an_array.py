# 2 ways: implementing quicksort and using built in sorted().


class Solution1:
    """Quicksort.
    Runtime: 276 ms, faster than 65.75%.
    Memory Usage: 20.2 MB, less than 20.71%."""

    def sortArray(self, nums: List[int]) -> List[int]:
        list_len = len(nums)
        if list_len < 2:
            return nums

        # Choose pivot
        # pivot = nums[list_len//2]
        pivot = nums[0]
        pivots = [num for num in nums if num == pivot]
        less = [num for num in nums if num < pivot]
        more = [num for num in nums if num > pivot]
        return self.sortArray(less) + pivots + self.sortArray(more)


class Solution2:
    """Built in sorted() function.
    Runtime: 120 ms, faster than 99.09%.
    Memory Usage: 20.2 MB, less than 73.02%."""

    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
