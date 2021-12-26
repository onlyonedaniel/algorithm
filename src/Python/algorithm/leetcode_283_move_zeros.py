from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 知道是0所以可以直接覆盖
        nums_len = len(nums)
        num_count = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[num_count] = nums[i]
                num_count += 1
        zero_count = nums_len - num_count
        if zero_count > 0:
            nums[-zero_count:] = [0 for i in range(zero_count)]
