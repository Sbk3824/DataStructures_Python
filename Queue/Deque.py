#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:26:00 2018

@author: sbk
"""

class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
d= Deque()
d.is_empty()

d.add_rear(4) # 4
d.add_rear('Dog') # Dog, 4
d.add_rear('Cat') # Cat, Dog , 4
d.size() # Size = 3
d.add_front(8.4) # Cat, Dog, 4, 8.4
d.remove_rear() # Cat is removed
d.remove_front() # 8.4 is removed
d.size() # Size = 2

