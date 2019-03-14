#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:18:55 2019

@author: sbk
"""

def generate_balanced_parentheses(num_pairs):
    def directed_b_p(left,right,valid,res = []):
        if left > 0:
            directed_b_p(left - 1, right, valid + '(')
        if left < right:
            directed_b_p(left, right - 1, valid + ')')
        if not right:
            res.append(valid)
        return res
    
    return directed_b_p(num_pairs, num_pairs, '')

generate_balanced_parentheses(2)