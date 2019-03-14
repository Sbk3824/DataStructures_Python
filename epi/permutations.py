#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:16:13 2019

@author: sbk
"""

def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            print(result)
            return
    
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
        
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]
        
    result = []
    directed_permutations(0)
    return result
    
A = [7,3,5]
permutations(A)


        
    