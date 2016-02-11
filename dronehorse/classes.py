#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""classes

Defines useful classes for use in drone direction project.

"""

from enum import Enum 

__status__ = "Development"
__version__ = "0.0.0"
__authors__ = ["Blaine Rogers <blaine.rogers14@imperial.ac.uk>",
               "Elliot Steele <elliot.steele14@imperial.ac.uk>",
               "Jonathan Sutton <jonathan.sutton14@imperial.ac.uk>"]

class SquashedHorseException(Exception):
    """Excpetion thrown when a horse become overloaded."""
    pass

class Move_type(Enum):
    deliver = 0
    load = 1

class Horse_state(Enum):
    passive = 0
    active = 1
    
class Dest_type(Enum):
    warehouse = 0
    house = 1

class Order():
    """An order from a customer."""

    def __init__(self, order_id, dest, no_items):
        """Initalises the order.

        Args:
            order_id (int): The (unique) id of the order.
            dest ((int, int)): The square of the grid that the items must be
                    delivered to.
            no_items (int): The number of items that must be delivered.

        """
        self.order_id = order_id
        self.dest = dest
        self.items = [0] * no_items
        
    def add_item(self, item, amount):
        """Adds an item to the order.

        Args:
            item (Item): The item to add it the order.
            amount (int): The amount of the item to add.

        """
        self.items[item] = amount



class Horse():
    """Definitely not a drone."""

    def __init__(self, pos, max_load, no_contents):
        """Initialises the horse.

        Args:
            pos ((int, int)): The position on the grid of the horse.
            max_load (int): The maximum load of the horse.

        """
        self.pos = pos
        self.max_load = max_load
        self.current_load = 0
        self.state = Horse_state.passive
        self.countdown = 0
        self.contents = [0]*no_contents
        
    def add_items(self, items, weights):
        """Adds items to the horse's load.

        Args:
            items ({Item -> int}): A dictionary of items and amounts.

        Examples:
            >>> h = Horse((0, 0), 5)
            >>> a = Item(0, 2)
            >>> b = Item(1, 1)
            >>> h.add_items({a: 2, b: 1}) # load horse to max capacity
            >>> h # doctest: +NORMALIZE_WHITESPACE
            <horse @(0, 0) with {<item 0>: 2, <item 1>: 1}>

        """
        for i in range(0,len(items)):
            self.contents[i] += items[i]
            self.current_load += weights[i]
            if self.current_load > self.max_load:
                raise SquashedHorseException("NeighSPLAT")
    
    def remove_items(self, items, weights):
        """Removes items from the horse's load.

        Args:
            items ({Item -> int}): A dictionary of items and amounts.

        Examples:
            >>> h = Horse((0, 0), 5)
            >>> a = Item(0, 2)
            >>> b = Item(1, 1)
            >>> h.add_items({a: 2, b: 1}) # load horse to max capacity
            >>> h.remove_items({a: 1})
            >>> h # doctest: +NORMALIZE_WHITESPACE
            <horse @(0, 0) with {<item 0>: 1, <item 1>: 1}>

        """
        for i in range(0,len(items)):
            self.contents[i] -= items[i]
            self.current_load -= weights[i]

    def __repr__(self):
        return "<horse @{} with {}>".format(self.pos, self.items)
            
        
class Warehouse():
    def __init(self, pos, no_contents):
        self.pos = pos
        self.contents = [0]*no_contents
        
    def add_items(self, items):
        for i in range(0,len(items)):
            self.contents[i] += items[i]
    
    def remove_items(self,items):
        for i in range(0,len(items)):
            self.contents[i] -= items[i]
        
        
class State():
    def __init__(self, size, no_horses, turns, max_horse_weight):
        self.size = size
        self.no_horses = no_horses
        self.turns = turns
        self.horses = []
        self.warehouses = []
        self.orders = []
        self.weights = []
        
    def add_horse(self, horse):
        self.horses.append(horse)
        
    def add_warehouse(self,warehouse):
        self.warehouses.append(warehouse)
        
    def add_order(self,order):
        self.orders.append(order)
    
    def add_weights(self, weights):
        self.weights = weights
        
        
class Move():
    def __init__(self, move_type, horse_id, dest_id, item, amount):
        self.move_type = move_type
        self.horse_id = horse_id
        self.dest_id = dest_id
        self.item = item
        self.amount = amount
