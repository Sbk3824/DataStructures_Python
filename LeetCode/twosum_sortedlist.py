#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 02:32:27 2019

@author: sbk
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, n = 0, len(numbers) - 1
        while i < n:
            if numbers[i] + numbers[n] == target:
                return [i + 1, n + 1]
            elif numbers[i] + numbers[n] > target:
                n -= 1
            else:
                i += 1
        return [-1,-1]
        