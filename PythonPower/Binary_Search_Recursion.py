#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:58:09 2018

@author: sbk
"""


def binary_search(a_list, item):
    first = 0
    last =len(a_list)-1
    found = False
    while first<=last and not found:
        mid = (first+last)//2
        if a_list[mid] == item:
            found = True
        elif a_list[mid] > item:
            return binary_search(a_list[:mid], item)
        else:
            return binary_search(a_list[mid + 1:], item)
            
    return found


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))