# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def isBadVersion(version, bad_version=40):
    return bad_version <= version


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        if isBadVersion(start):
            return start
        while True:
            mid = int((end + start) / 2)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid

            # 确定终止条件
            if (end - start) == 1:
                return end
