#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Q2Stacks.py
#  
#  Copyright 2020 phbrown <phbrown@KUH-212-CLPC>
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
from typing import List, Generic, TypeVar
from Stack import Stack

T = TypeVar('T')

class Queue(Generic[T]):
    """Implement a queue by means of two stacks."""
    
    def __init__(self) -> None:
        """Create an empty queue."""
        self._inbox = Stack[T]()  # Items get pushed here
        self._outbox = Stack[T]() # Items get popped from here

    # Query methods
    def empty(self) -> bool:
        """Return True if the queue is empty, else False."""
        # Only empty if both stacks are empty
        return self._inbox.empty() and self._outbox.empty()
        
    def peek(self) -> T:
        """Look at the item at the head of the queue and return
        its value.  Do not remove it from the queue."""
        # If there's something in the outbox, this is just a regular peek()
        # If there's nothing in the outbox, refill it from the inbox
        #     and then peek()
        if self._outbox.empty():    # True only 1/n of the time
            self._fillOutbox()          # O(n)
        return self._outbox.peek()  # O(1)
        
    # Mutator methods
    def _fillOutbox(self) -> None:
        """Move any items in the inbox to the outbox."""
        # Popping things from the inbox produces them in reverse order
        # Pushing them into the outbox reverses the order *again*
        # So they will pop from the outbox in the correct order (FIFO)
        while not self._inbox.empty():  # O(n) times around the loop
            self._outbox.push(self._inbox.pop()) # O(1)
    
    def push(self, item:T) -> None:
        """Append the given ITEM to the queue."""
        # Just push it into the inbox
        self._inbox.push(item)    # O(1)
    
    def pop(self) -> T:
        """Pop the first item off the queue."""
        # If there's something in the outbox, just pop it
        # If there's nothing in the outbox, refill it from the inbox
        #     and *then* pop the outbox
        if self._outbox.empty():  # True only 1/n of the time
            self._fillOutbox()        # O(n)
        return self._outbox.pop() # O(1)

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
