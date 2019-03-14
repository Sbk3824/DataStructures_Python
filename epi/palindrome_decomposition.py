#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:38:52 2019

@author: sbk
"""

def palindrome_decompositions(input):
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(input):
            result.append(list(partial_partition))
            print(result)
            return
        
        for i in range(offset + 1, len(input) + 1):
            prefix = input[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(i, partial_partition + [prefix])
                
    result = []
    directed_palindrome_decompositions(0, [])
    return result

input_raw = '0204451881'
palindrome_decompositions(input_raw)