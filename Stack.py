# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import List, Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    """Class to implement a generic stack."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self.items:List[T] = []

    # Query functions
    def empty(self) -> bool:
        """Return whether the stack is empty."""
        return (len(self.items) == 0)

    def peek(self) -> T:
        """Look at the top object, without removing it from the stack."""
        # Precondition:
        assert not self.empty()
        return self.items[-1]
        # Postcondition: nothing changed

    # Mutator functions
    def push(self, item:T) -> None:
        """Put something on top of the stack."""
        self.items.append(item)
        # Postcondition: stack grew by one item, and...
        assert self.items[-1] == item

    def pop(self) -> T:
        """Remove and return the top item from the stack."""
        # Precondition:
        assert not self.empty()
        return self.items.pop()
        # Postcondition: the stack is now one item smaller

def main(args:List[str]) -> int:
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))