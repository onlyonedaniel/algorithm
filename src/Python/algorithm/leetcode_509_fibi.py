class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return 1
        else:
            i = 2
            while i <= n:
                a, b = b, a + b
                i += 1
            return b
