# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle 
colors = ['red', 'purple', 'blue','orange', 'yellow','green'] 
t = turtle.Pen() 
turtle.bgcolor('black')
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(10) 
    t.forward(x) 
    t.left(59)
    if x==50:
        t.backward(x-20)
    if x==100:
        t.backward(x-20)
    if x==150:
        t.backward(x-20)
    if x==200:
        t.backward(x-20)
    if x==250:
        t.backward(x-20)
