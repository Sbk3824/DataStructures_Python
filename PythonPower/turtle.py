#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 23:51:44 2018

@author: sbk
"""

import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


draw_spiral(my_turtle, 100)
my_win.exitonclick()