#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:11:55 2019

@author: sbk
"""

 
num_words = 0
 
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        
print("Number of words:")
print(num_words)