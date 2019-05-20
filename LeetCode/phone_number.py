#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 01:25:17 2019

@author: sbk
"""

def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_ = { '2' : 'abc', '3' : 'def', '4' : 'ghi',  '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv',
            '9' : 'wxyz'}
            
        result = []
        
        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map_[digits[i]]:
                cur.append(ch)
                make_combinations(i+1, cur)
                cur.pop()
        
        make_combinations(0, [])
        
        return result
    
letterCombinations('23')