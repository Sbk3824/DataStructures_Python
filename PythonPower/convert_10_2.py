#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:52:55 2018

@author: sbk
"""

import Stack 

def divide_by_2(dec_number):
    rem_stack = Stack.Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
        
    return bin_string

print(divide_by_2(42))