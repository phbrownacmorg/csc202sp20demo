#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  CircQ.py: circular queue
#  
#  Copyright 2019 phbrown <phbrown@KUH-212-CLPC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from typing import List, Generic, Optional, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Implement a circular queue by wrapping a Python list.  Basically,
    the idea is that empty slots hold the value None, while full slots
    hold something else.  

    The queue can grow if it gets full, although it doesn't ever
    shrink.  When it grows, it doubles in capacity (just like a Python
    list)."""
    
    def __init__(self) -> None:
        """Create an empty queue."""
        # Initial capacity == 4
        self._items:List[Optional[T]] = [None] * 4
        self._head = 0 # Index
        self._tail = 0 # Index

    # Query methods
    def empty(self) -> bool:
        """Return True if the queue is empty, else False."""
        return (self._head == self._tail) and \
                (self._items[self._head] == None)  # O(1)
        
    def peek(self) -> Optional[T]:
        """Look at the item at the head of the queue and return
        its value.  Do not remove it from the queue."""
        return self._items[self._head]     # O(1)
        
    # Mutator methods
    def push(self, item:T) -> None:
        """Append the given ITEM to the queue."""
        if self._items[self._tail] != None: # Queue is full, resize
            # This is an O(n) operation, which happens 1/n of the time
            newItems:List[Optional[T]] = [None] * (2 * len(self._items))
            itemCount = 0
            while not self.empty(): # Copy everything across
                newItems[itemCount] = self.pop()
                itemCount = itemCount + 1
            self._items = newItems
            self._head = 0
            self._tail = itemCount
        # Queue is no longer full, go ahead and push
        self._items[self._tail] = item                   # O(1)
        self._tail = (self._tail + 1) % len(self._items) # O(1)
    
    def pop(self) -> Optional[T]:
        """Pop the first item off the queue."""
        value = self._items[self._head]                  # O(1)
        self._items[self._head] = None                   # O(1)
        self._head = (self._head + 1) % len(self._items) # O(1)
        return value

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
