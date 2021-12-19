# import sys

from ..algorithm import (
    leetcode_35_insert_position,
    leetcode_278_find_first_bad_version,
    leetcode_704_bineray_search,
)


def test_binary_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = leetcode_704_bineray_search.Solution().search(nums, target)
    assert result == 4


def test_bad_version():
    n = 100
    result = leetcode_278_find_first_bad_version.Solution().firstBadVersion(n)
    assert result == 40


def test_search_insert():
    nums = [1, 3, 5, 6]
    target = 2
    result = leetcode_35_insert_position.Solution().searchInsert(nums, target)
    assert result == 1
