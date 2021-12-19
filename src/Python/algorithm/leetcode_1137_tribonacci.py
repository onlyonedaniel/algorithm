class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return t0
        elif n == 1:
            return t1
        elif n == 1:
            return t2
        else:
            i = 3
            while i <= n:
                t0, t1, t2 = t1, t2, t0 + t1 + t2
                i += 1
            return t2
