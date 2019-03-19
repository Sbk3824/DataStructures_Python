#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:02:00 2019

@author: sbk
"""

def minHeapify(heap,index):
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index
    if len(heap) > left and heap[smallest] > heap[left]:
      smallest = left
    if len(heap) > right and heap[smallest] > heap[right]:
      smallest = right
    if smallest != index:
      tmp = heap[smallest]
      heap[smallest] = heap[index]
      heap[index] = tmp
      minHeapify(heap,smallest)
    return heap

def convertMax(maxHeap):
  for i in range((len(maxHeap))//2,-1,-1):
    maxHeap = minHeapify(maxHeap,i)
  return maxHeap
  
maxHeap = [9,4,7,1,-2,6,5]
print(convertMax(maxHeap))