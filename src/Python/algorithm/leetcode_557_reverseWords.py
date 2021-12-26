class Solution:
    def reverseWords(self, s: str) -> str:
        temp = list(s)
        left = 0
        indent = 0
        len_ = len(temp) - 1
        for index, value in enumerate(temp):
            if value == " " or index == len_:
                if index == len_:
                    right = index
                else:
                    right = index - 1
                indent = index
                while right > left:
                    temp[right], temp[left] = temp[left], temp[right]
                    left += 1
                    right -= 1
                left = indent + 1

        return "".join(temp)
