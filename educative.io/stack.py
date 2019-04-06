#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:19:53 2019

@author: sbk
"""

class myStack:
    def __init__(self):
        self.stackList = []
        
    def size(self):
        return len(self.stackList)
    
    def isEmpty(self):
        return self.size() == 0
    
    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]
    
    def push(self,e):
        self.stackList.append(e)
        
    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()
    
    def print_stack(self):
        if self.isEmpty():
            return None
        for i in range(self.size()):
            print(self.stackList[i])
        return None
    
    
stack = myStack()
print("isEmpty(): " + str(stack.isEmpty()))
print("top() " + str(stack.top()))
print("size() " + str(stack.size()))

stack.push(10)
stack.push(20)

stack.pop()

stack.print_stack()