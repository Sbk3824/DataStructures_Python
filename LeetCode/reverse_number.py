class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        n = 0
        while x > 0:
            n = n * 10 + (x % 10)
            x /=10
        if -(2**31)-1 < n < 2**31:
            if neg:
                return -n
            return n
        return 0
        