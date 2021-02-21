# 2 ways: implementing quicksort and using built in sorted().


class Solution1:
    """Trivial Quicksort-like implementation.
    Runtime: 232 ms, faster than 80.16%.
    Memory Usage: 21.3 MB, less than 25.51%."""

    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            list_len = len(nums)
            if list_len < 2:
                return nums

            # Choose pivot
            # pivot = nums[list_len//2]
            pivot = nums[0]

            pivots = []
            less = []
            more = []
            for num in nums:
                if num < pivot:
                    less.append(num)
                elif num == pivot:
                    pivots.append(num)
                else:
                    more.append(num)
            return self.sortArray(less) + pivots + self.sortArray(more)


class Solution2:
    """Built in sorted() function.
    Runtime: 120 ms, faster than 99.09%.
    Memory Usage: 20.2 MB, less than 73.02%."""

    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
