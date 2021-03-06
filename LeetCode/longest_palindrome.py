#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:51:44 2019

@author: sbk
"""

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = " "
        for i in range(len(s)):
            temp = self.helper(s,i,i)
            if len(temp) > len(res):
                res = temp
                
            temp = self.helper(s,i,i + 1)
            if len(temp) > len(res):
                res = temp
        return res
    
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1 : r]