#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program that counts how amny ways you can go 
from the top-left to the bottom-right in a 2-D aarry
"""

def uniquePaths( m, n):
        def compute_xy( x , y):
            if x == y == 0:
                return 1
            
            if number_of_ways[x][y] == 0:
                ways_top = 0 if x == 0 else compute_xy(x-1,y)
                ways_left = 0 if y == 0 else compute_xy(x,y -1)
                number_of_ways[x][y] = ways_top + ways_left
            return number_of_ways[x][y]
    
        number_of_ways = [[0] * n for _ in range(m)]
        return compute_xy( m -1 , n -1)
    
uniquePaths(5,5)
            