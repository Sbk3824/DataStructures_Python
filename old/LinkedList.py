#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:14:28 2018

@author: sbk
"""

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

temp = Node(93)
temp.get_data()

  

class UnorderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    

mylist = UnorderedList()
      
