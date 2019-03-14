#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:46:59 2019

@author: sbk
"""

def genereate_power_set(input_set):
    def directed_power_set(tobe_selected, selected_sofar):
        if tobe_selected == len(input_set):
            power_set.append(list(selected_sofar))
            return
        
        directed_power_set(tobe_selected + 1, selected_sofar)
        directed_power_set(tobe_selected + 1, selected_sofar + [input_set[tobe_selected]])
    
    
    power_set = []
    directed_power_set(0, [])
    return power_set


input_set = [0,1,2]
genereate_power_set(input_set)