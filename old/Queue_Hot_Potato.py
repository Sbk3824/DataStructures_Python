#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 23:59:43 2018

@author: sbk
"""

import Queue # As previously defined

def hot_potato(name_list, num):
    sim_queue = Queue.Queue()
    for name in name_list:
        sim_queue.enqueue(name)
        
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7))