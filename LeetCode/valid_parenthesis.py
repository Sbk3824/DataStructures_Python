#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:05:17 2019

@author: sbk
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for char in s:
            if char in dict:
                stack.append(char)
            elif not stack or dict[stack.pop()] != char:
                return False
        return not stack