class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        offset = len(nums1) - m
        i = 0
        while i < len(nums1) and nums2:
            num = nums1[i]
            num2 = nums2[0]

            if num2 < num:
                nums1.insert(i, num2)
                nums2.pop(0)
            i += 1

        if i >= len(nums1) and nums2 is not None:
            nums1[len(nums1) - offset:] = nums2
        while len(nums1) > m + n:
            nums1.pop()
