#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Queue.py
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
from typing import List, Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Implement a queue by wrapping a Python list.  The end
    of the list is the end of the queue."""
    
    def __init__(self) -> None:
        """Create an empty queue."""
        self._items:List[T] = []

    # Query methods
    def empty(self) -> bool:
        """Return True if the queue is empty, else False."""
        return (len(self._items) == 0)
        
    def peek(self) -> T:
        """Look at the top item on the queue and return its value.
        Do not remove it from the queue."""
        return self._items[0]
        
    # Mutator methods
    def push(self, item:T) -> None:
        """Append the given ITEM to the queue."""
        self._items.append(item)
    
    def pop(self) -> T:
        """Pop the first item off the queue.  If the Queue is
        implemented as a Python list, this is slow."""
        return self._items.pop(0)

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
