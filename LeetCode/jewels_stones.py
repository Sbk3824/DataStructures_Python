class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d, count = {}, 0
        for ch in J:
            d[ch] = 0
        for ch in S:
            if ch in d:
                count += 1
        return count
        