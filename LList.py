#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  LList.py
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

from typing import Any, cast, List, Optional

class LList(object):
    """Implements a linked list with a sentinel node indicating an empty
    list.  The sentinel node has both data and next equal to None.  No
    methods are provided to get or set the internal attributes of a
    list node directly, so as to discourage mucking about with the list
    without using the ADT methods."""

    def _invariant(self) -> bool:
        """Class invariant.  This actually checks the entire list."""
        valid = False
        if (self._next != None): # Normal node, check the next one
            # (We already know self._next != None, so the cast will work.)
            valid = cast(LList, self._next)._invariant()
        elif (self._next == None and self._data == None): # Sentinel
            valid = True
        return valid
        
    def __init__(self) -> None:
        """Create an empty list node."""
        self._data:Any = None
        self._next:Optional[LList] = None
        # Post
        assert self._invariant()
        
    # Query methods
    
    def isEmpty(self) -> bool:
        """Returns True if the list is empty, False otherwise."""
        # True if this is the sentinel node
        return self._data == None and self._next == None 
        
    def size(self) -> int:
        """Returns the number of items on the list."""
        if self.isEmpty(): # No nodes, just return 0
            return 0
        else: # return 1 for this node, plus the size of the rest of the list
            # (We already know there *is* more list, so the cast will work.)
            return 1 + cast(LList, self._next).size()

    def search(self, value:Any) -> bool:
        """Searches the list for value VALUE and returns a Boolean
        indicating that VALUE is present in the list (True) or not
        present in the list (False)."""
        if self.isEmpty(): # Empty list contains nothing
            return False
        elif self._data == value: 
            # If this node has the right contents, return True
            return True
        else:
            # Otherwise, ask the rest of the list
            # (We already know there *is* more list, so the cast will work.)
            return cast(LList, self._next).search(value)

    def __str__(self) -> str:
        """Returns a tring representation of the list."""
        if self.isEmpty(): # Show the sentinel node
            return "\u2205" #\u22a3, 252b
        else: # Show this node, and concatenate on the rest of the list
            # 27f6, 27f9
            return "\u276c{}\u276d\u279e".format(self._data) + str(cast(LList, self._next))
        
    def shallowCopy(self) -> 'LList':
        """Returns a shallow copy of the list, only copying pointers."""
        return self

    def deepCopy(self) -> 'LList':
        """Returns a deep(er) copy of the list, copying data."""
        newList:LList = LList() # if self is empty, this is the right value
        if not self.isEmpty():
            # Cast is safe because we already know self._next != None
            newList = cast(LList, self._next).deepCopy()
            newList.add(self._data)
        return newList


    # Mutator methods
    
    def add(self, value:Any) -> None:
        """Adds a new node containing VALUE to the head of the list."""
        newNode = LList() # Empty node
        
        # Copy the contents of the current head to the new node
        newNode._next = self._next
        newNode._data = self._data

        # Link to the new node (effectively, to the old head)
        self._next = newNode
        # Put the new data in the head node (now the new head)
        self._data = value
        # Post:
        assert self._invariant()
        
    def pop(self, pos:int = -1) -> Any:
        """Pops the item at position POS off the list, 
        and returns it."""
        # Pre:
        assert (not (self.isEmpty())) # Can't pop from an empty list
        size = self.size() 
        assert -size <= pos < size # Make sure POS argument is valid

        # Handle negative indexes in POS
        if pos < 0:
            pos = pos + size
        assert pos >= 0
        
        result = None # Make sure there *is* a result available to return
        if pos == 0: # Pop this node
            result = self._data # Data to return
            
            # (We know the list isn't empty, so there *is* a node there.)
            nextNode:LList = cast(LList, self._next)
            
            # Copy the next node's contents into this node.
            # The effect is to link around the next node.
            self._data = nextNode._data
            self._next = nextNode._next
        else: # pos > 0, so we count down pos until pos == 0
            # Popping position POS from here is the same as popping position
            #    POS - 1 from the rest of the list
            # (We already know there *is* more list, so the cast will work.)
            result = cast(LList, self._next).pop(pos - 1)
            
        # Post:
        assert self._invariant()
        return result
   

def main(args:List[str]) -> int:
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
