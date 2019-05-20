#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:03:11 2019

@author: sbk
"""

class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.data = key 
        
def inOrder(tree):
    stack = []
    done = 0
    current = tree
    
    while(not done):
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.data)
                current = current.right
            
            else:
                done = 1
                
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
inOrder(root) 
            
    