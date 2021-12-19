class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            i = 3
            while i <= n:
                a, b = b, a + b
                i += 1

            return b
