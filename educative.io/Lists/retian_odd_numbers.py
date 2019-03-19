#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:32:41 2019

@author: sbk
"""

def removeEven(comp_list):
    return [item for item in comp_list if item % 2 != 0]

comp_list = [9,3,4,6,3,4,8,0,1]
removeEven(comp_list)