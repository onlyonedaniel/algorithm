# 题目链接：https://leetcode-cn.com/problems/binary-search/
from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 递归解法
        if len(nums) == 0:
            return -1
        nums_len = len(nums)
        begin = 0
        end = nums_len - 1

        if nums[begin] == target:
            return begin
        if nums[end] == target:
            return end
        if target < nums[begin] or target > nums[end]:
            return -1
        # 查找区间为 [begin, end]
        return self.binary_search(nums, begin, end, target)

    def binary_search(self, nums: List[int], begin: int, end: int, target: int) -> int:
        if begin == end and nums[begin] != target:
            return -1
        mid = int((end + begin) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, begin, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, end, target)
