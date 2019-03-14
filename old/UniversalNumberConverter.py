#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:06:54 2018

@author: sbk
"""

import Stack 

def divide_by_2(dec_number,base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack.Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
        
    return new_string

print(divide_by_2(42,2))