#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:45:10 2019

@author: sbk
"""


# Brute Force
"""
def findProduct(arr):
  temp = []
  for i in range(len(arr)):
    sum = 1
    for j in range(len(arr)):
      if i != j:
        sum *= arr[j]
    temp.append(sum)
  return temp

findProduct([1,2,3,4])

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