#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:14:35 2018

@author: sbk
"""

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp

a_list = [1,3,2,6,4]
print(len(a_list))
selection_sort(a_list)
print(a_list)