# import sys

from ..algorithm import leetcode_704_bineray_search


def test_binary_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = leetcode_704_bineray_search.Solution().search(nums, target)
    assert result == 4
