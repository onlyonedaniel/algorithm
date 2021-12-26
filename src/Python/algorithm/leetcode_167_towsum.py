from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        len_nums = len(numbers)
        right = len_nums - 1
        while right > left:
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
