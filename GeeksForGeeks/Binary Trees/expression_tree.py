#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:01:39 2019

@author: sbk
"""

# Python program to insert element in binary tree 
class Tree: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		
# A utility function to do inorder traversal 
def inorder(t): 
    if t is not None: 
        inorder(t.left) 
        print(t.data)
        inorder(t.right) 
    
    
def isOperator(value):
    operators = ['+','-','*','/','%']
    if value in operators:
        return True
    return False
    
   
def postfix_convertor(expr):
    stack = []
    
    for char in expr:
        if not isOperator(char):
            t = Tree(char)
            stack.append(t)
        else:
            t = Tree(char)
            s1 = stack.pop()
            s2 = stack.pop()
            
            t.right = s1
            t.left = s2
            
            stack.append(t)
    t = stack.pop()
    return t


postfix = "ab+ef*g*-"
r = postfix_convertor(postfix) 
print("Infix expression is")
inorder(r) 