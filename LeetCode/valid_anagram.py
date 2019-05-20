class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for char in s:
            d1[char] = d1.get(char, 0) + 1
        for char in t:
            d2[char] = d2.get(char, 0) + 1
        return d1 == d2
            