#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:46:30 2019

@author: sbk
"""

class Node: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
        
def is_foldable(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 and root2:
        return(is_foldable(root1.left, root2.right) and
               is_foldable(root1.right, root2.left))
        
    return False

def check_foldable(root):
    return is_foldable(root.left, root.right)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4) 
root.left.right = Node(5) 


print("1" if check_foldable(root) == True else "0")
