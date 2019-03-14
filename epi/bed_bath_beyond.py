#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:39:21 2019

@author: sbk
"""

def word_break(domain, dictionary):
    last_length = [-1] * len(domain)
    
    for i in range(len(domain)):
        print('---------')
        print(i)
        print(domain[:i+1])
        if domain[:i+1] in dictionary:
            last_length[i] = i + 1
        print(last_length[i])
        
        
        if last_length[i] == -1:
            for j in range(i):
                print(j)
                if last_length[j] != -1 and domain[j+1:i+1] in dictionary:
                    last_length[i] = j + 1
                    print(last_length[i])
                    print('------BREAK-----')
                    break

    
    decompositions = []
    if last_length[-1] != -1: 
        idx = len(domain) -1
        while idx >= 0:
            decompositions.append(domain[idx+1-last_length[idx]:idx + 1])
            idx -=last_length[idx]
        decompositions = decompositions[::-1]
        
    return decompositions
            


s = 'leetcode'
wordDict = ["leet", "code"]
word_break(s, wordDict)