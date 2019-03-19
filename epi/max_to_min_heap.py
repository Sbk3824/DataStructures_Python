#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:31:26 2019

@author: sbk
"""

def sum_close_3(data, target):
    min_d, idx, f_sum = target, 0, 0
    for i in range(len(data)):
        sum_d = 0
        for j in range(len(data)):
            if i == j:
                continue
            sum_d += data[j]


        
        if abs(sum_d - target) <= min_d:
            min_d, idx = abs(sum_d - target), i


    for k in range(len(data)):
        if idx == k:
            continue
        f_sum += data[k]
    print(f_sum)

     
        
        
    
    
    
data = [-1,2,1,-4]
target = 1
sum_close_3(data, target)