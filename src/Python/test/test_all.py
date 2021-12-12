# import sys

from ..algorithm import leetcode_704_bineray_search, leetcode_278_find_first_bad_version


def test_binary_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = leetcode_704_bineray_search.Solution().search(nums, target)
    assert result == 4


def test_bad_version():
    n = 100
    result = leetcode_278_find_first_bad_version.Solution().firstBadVersion(n)
    assert result == 40
