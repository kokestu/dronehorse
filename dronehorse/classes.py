# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:13:10 2016

@author: Jonathan
"""

import Exception

class Squashed_horse_exception(Exception):
    pass

class Order():
    def __init__(self, order_id, dest, no_items):
        self.order_id = order_id
        self.dest = dest
        self.no_items = no_items
        self.items = dict()
        
    def add_item(self, item, amount):
        self.items[item] = amount
        
class Item():
    def __init__(self, item_id, weight):
        self.item_id = item_id
        self.weight = weight

class Horse():
    def __init__(self, pos, max_load):
        self.pos = pos
        self.max_load = max_load
        self.current_load = 0
        self.contents = dict()
        
    def add_items(self, items):
        for k, v in items:
            self.contents[k] += items[k]
            self.current_load += v.weight
            if self.current_load > self.max_load:
                raise Squashed_horse_exception("NeighSPLAT")
    
    def remove_items(self,items):
        for k, v in items:
            self.contents[k] -= items[k]
        
class Warehouse():
    def __init(self, pos, contents):
        self.pos = pos
        self.contents = dict()
        
    def add_items(self, items):
        for k, v in items:
            self.contents[k] += items[k]
    
    def remove_items(self,items):
        for k, v in items:
            self.contents[k] -= items[k]
        
class State():
    def __init__(self, size, turns, weights):
        self.size = size
        self.turns = turns
        self.weights = weights
        self.horses = []
        self.warehouses = []
        self.orders = []
        
    def add_horse(self, horse):
        self.horses.append(horse)
        
    def add_warehouse(self,warehouse):
        self.warehouses.append(warehouse)
        
    def add_order(self,order):
        self.orders.append(order)
