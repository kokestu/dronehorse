# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:13:10 2016

@author: Jonathan
"""

class order():
    def __init__(self,order_id,dest,no_items):
        self.order_id = order_id
        self.dest = dest
        self.no_items = no_items

class horse():
    def __init__(self,pos,max_load):
        self.pos = pos
        self.max_load = max_load
        self.contents = []
        
class warehouse():
    def __init(self,pos,contents):
        self.pos = pos
        self.contents = contents
        
class state():
    def __init__(self,size,turns,weights):
        self.size = size
        self.turns = turns
        self.weights = weights
