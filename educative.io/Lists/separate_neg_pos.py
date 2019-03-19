#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:25:51 2019

@author: sbk
"""

def reArrange(lst):
  return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(reArrange([-1, 2, -3, -4, 5]))
print(reArrange([300, -1, 3, 0]))
print(reArrange([0, 0, 0, -2]))