from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = k % nums_len
        if k > 0:
            temp = nums[-k:]
            nums[k:] = nums[:-k]
            nums[:k] = temp
