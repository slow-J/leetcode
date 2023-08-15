class Solution:
    def searchInsert_(self, nums: List[int], target: int) -> int:
        # simple branchless binary search!!!!
        first = 0
        length = len(nums)
        while (length > 0):
            rem = length % 2
            length //= 2

            if nums[first + length] < target:
                first += length + rem
        return first


    def searchInsert_advanced(self, nums: List[int], target: int) -> int:
        # more advanced branchless binary search
        first = 0
        length = len(nums)
        while length & (length + 1):
            step = length // 8 * 6 + 1
            if nums[first + step] < target:
                first += step + 1
                length -= step + 1
            else:
                length = step
                break
        while length != 0:
            length //= 2
            if nums[first + length] < target:
                first += length + 1
        return first
