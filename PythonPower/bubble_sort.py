#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:53:07 2018

@author: sbk
"""
'''
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


a_list = [2,6,3,5,4]
bubble_sort(a_list)
print(a_list)
'''


# Short bubble sort with stop function when the list is ordered.

def bubble_sort(a_list):
    ordered = True
    pass_num = len(a_list)-1
    while pass_num > 0 and ordered:
        ordered = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                ordered = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

    pass_num = pass_num -1
        
a_list = [2,6,3,5,4]
bubble_sort(a_list)
print(a_list)