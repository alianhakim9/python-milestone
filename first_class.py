#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:24:49 2021

@author: alian
"""

# ini adalah comment


class Point:
    
    def __init__(self, x,y):
        self.move(x, y)
    
    def move(self,x,y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(0,0)
        
    def tambah(self):
        return self.x + self.y
    
    