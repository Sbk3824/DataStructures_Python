#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:54:38 2019

@author: sbk
"""

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def generate_all_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]
    
    result = []
    for left_num in range(num_nodes):
        right_num = num_nodes - 1 - left_num
        left_tree = generate_all_binary_trees(left_num)
        right_tree = generate_all_binary_trees(right_num)
        
        result += [BinaryTreeNode(0, left, right) for left in left_tree for right in right_tree]
        
    return result

generate_all_binary_trees(3)