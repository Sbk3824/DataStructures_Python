#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:38:20 2019

@author: sbk
"""

def findProduct(lst):
  left = 1
  product = []
  for ele in lst:
    product.append(left)
    left = left * ele
    
  right = 1
  for i in range(len(lst)-1,-1,-1):
    product[i] = product[i] * right
    right = right * lst[i]
    
  return product

print(findProduct([1,2,3,4]))