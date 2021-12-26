# import sys

from ..algorithm import (
    leetcode_35_insert_position,
    leetcode_70_climbStairs,
    leetcode_189_rotate,
    leetcode_278_find_first_bad_version,
    leetcode_283_move_zeros,
    leetcode_509_fibi,
    leetcode_704_bineray_search,
    leetcode_977_sortedSquares,
    leetcode_1137_tribonacci,
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


def test_fibi():
    n = 2
    result = leetcode_509_fibi.Solution().fib(n)
    assert result == 1


def test_climbStarts():
    n = 3
    result = leetcode_70_climbStairs.Solution().climbStairs(n)
    assert result == 3


def test_tribonacci():
    n = 4
    result = leetcode_1137_tribonacci.Solution().tribonacci(n)
    assert result == 4


def test_rotate():
    nums = [1, 2]
    leetcode_189_rotate.Solution().rotate(nums, 2)
    assert nums[0] == 1


def test_move_zeros():
    nums = [1, 0, 1, 2, 0, 1]
    leetcode_283_move_zeros.Solution().moveZeroes(nums)
    assert nums == [1, 1, 2, 1, 0, 0]


def test_sorted_Squares():
    nums = [-3, -1, 0, 1, 2]
    result = leetcode_977_sortedSquares.Solution().sortedSquares(nums)
    assert result == [0, 1, 1, 4, 9]
