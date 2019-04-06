#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:04:55 2019

@author: sbk
"""

class myQueue:
    def __init__(self):
        self.queueList = []
    
    def isEmpty(self):
        return self.size() == 0
  
    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]
    
    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]
  
    def size(self):
        return len(self.queueList)
    
    def enqueue(self, e):
        self.queueList.append(e)
        
    def dequeue(self):
        if self.isEmpty():
            return None
        remove_el = self.front()
        self.queueList.remove(remove_el)
        return remove_el
    
    
def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)
      
    return result; #For number = 3 , result = {"1","10","11"};
  
print(findBin(3))