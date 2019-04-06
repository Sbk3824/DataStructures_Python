#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:52:45 2019

@author: sbk
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        
    def isEmpty(self):
        return self.head.next == None
    
    def getHead(self):
        if self.isEmpty():
            return False
        return self.head
    
    # Insert at head , O(1)
    def insertAtHead(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        return self.head
    
    # Insert at tail , O(n)
    def insertAtTail(self, data):
        node = Node(data)
        lst = self.head
        while lst.next != None:
            lst = lst.next
        lst.next = node
        return
    
    # Search
    def search(self, lsst, data):
        lst = lsst.head.next
        while lst.next != None and lst.data != data:
            lst = lst.next
        if lst.data == data:
            return True
        return False
    
    # Delete at head
    def deleteAtHead(self,lst):
        if lst.head.next != None:
            lst.head.next = lst.head.next.next
        return 
    
    # Delete Value
    def deleteValue(self, lsst, data):
        lst = lsst.head.next
        while lst.next != None and lst.data != data:
            lst = lst.next
        if lst.data == data:
            lst.data = lst.next.data
            lst.next = lst.next.next
        return 
        

    def length(self):
        lst = self.head
        count = 0
        if self.isEmpty():
            return count
        while lst.next != None:
            count += 1
            lst = lst.next
        return count
        
        
    def printList(self):
        if self.isEmpty():
            print('List is Empty')
            return False
        
        lst = self.head.next
        while lst.next != None:
            print(lst.data)
            lst = lst.next
        print(lst.data)
        return True


list = LinkedList()
list.insertAtHead(21)
list.insertAtHead(14)
list.insertAtHead(7)
list.insertAtHead(8)
list.insertAtHead(22)
list.insertAtHead(15)



def findNth(list,n):
    # Write - Your - Code
    count = list.length()
    print(count)
    if n < 0 or n > count:
        return -1
    
    if list.isEmpty():
        return -1
    
    first = second = list.getHead().next
    for _ in range(n):
        first = first.next
        
    while first is not None:
        first, second = first.next, second.next
    return second.data

print(findNth(list, 5))
print(findNth(list, 1))
print(findNth(list, 10))