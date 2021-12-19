from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找到元素
        # 终止条件
        # 1. x = target
        start = 0
        end = len(nums) - 1
        result = end + 1
        while start <= end:
            mid = int((end + start) / 2)
            if target <= nums[mid]:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result
