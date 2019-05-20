#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:53:30 2019

@author: sbk
"""

# Python program to for tree traversals 

# A class that represents an individual node in a Binary Tree 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


# A function to do inorder tree traversal 
def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val)
		printInorder(root.right) 



# A function to do postorder tree traversal 
def printPostorder(root):
	if root:
		printPostorder(root.left) 
		printPostorder(root.right) 
		print(root.val), 


# A function to do preorder tree traversal 
def printPreorder(root): 
	if root: 
		print(root.val), 
		printPreorder(root.left) 
		printPreorder(root.right) 


# Driver code 
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print("Preorder traversal of binary tree is")
printPreorder(root) 

print("\nInorder traversal of binary tree is")
printInorder(root) 

print("\nPostorder traversal of binary tree is")
printPostorder(root) 
