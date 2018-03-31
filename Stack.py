#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:33:25 2018

@author: sbk
"""

# Completed implementation of a stack ADT

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
s = Stack()

print(s.is_empty())

s.push(4)
s.push('dog')

print(s.peek())

s.push(True)

print(s.size())
print(s.is_empty())

s.push(8.4)

print(s.pop())
print(s.pop())
print(s.size())