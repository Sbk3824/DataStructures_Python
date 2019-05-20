#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:39:23 2019

@author: sbk
"""

class Node: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
        
def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 and root2:
        return(root1.data == root2.data and 
               is_mirror(root1.left, root2.right) and
               is_mirror(root1.right, root2.left))
        
    return False

def is_symmetrical(root):
    return is_mirror(root.left, root.right)


root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 
print("1" if is_symmetrical(root) == True else "0")