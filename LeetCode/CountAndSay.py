class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def next_number(s):
            res, i = [], 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                res.append(str(count) + s[i])
                i += 1
            return ''.join(res)
        
        s = '1'
        for _ in range(1, n):
            s = next_number(s)
        return s
        