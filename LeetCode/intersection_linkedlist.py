#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 02:23:37 2019

@author: sbk
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        curA, curB = headA, headB
        lenA = lenB = 0
        while curA:
            lenA += 1
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next
        
        if lenA > lenB:
            diff = lenA - lenB
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            diff = lenB - lenA
            while diff > 0:
                headB = headB.next
                diff -= 1
                
        while headA and headB:
            if headA != headB:
                headA = headA.next
                headB = headB.next
            else:
                return headA
            
        