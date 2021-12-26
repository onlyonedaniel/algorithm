from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        result: List[int] = []
        while end >= start:
            end_result = nums[end] * nums[end]
            start_result = nums[start] * nums[start]
            if end_result >= start_result:
                result.insert(0, end_result)
                end -= 1
            else:
                result.insert(0, start_result)
                start += 1
        return result
