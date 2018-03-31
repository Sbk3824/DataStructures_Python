#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 23:53:26 2018

@author: sbk
"""

# Completed implementation of a queue ADT
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.size()
q.dequeue()