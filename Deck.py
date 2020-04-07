# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import Iterable, TypeVar, Generic, List
from AbstractCard import AbstractCard

# Idea here is to use the same class for different kinds of AbstractCards,
#   *without* allowing Decks to mix types of cards.  (Note that if you *want*
#   to allow a deck of mixed-type cards, you can always create your Deck as 
#   Deck[AbstractCard].)
T = TypeVar('T') 

class Deck(Generic[T]):
    """Class to represent a deck of cards.  The card at position 0 is on the bottom of the deck."""

    def __init__(self, cards:Iterable[T]) -> None:
        # Pre: T is a subclass of AbstractCard
        self._cards:List[T] = []
        for card in cards:
            self._cards.append(card)
        # Post: Every item in self._cards has class T

    # Query methods
    def __len__(self) -> int:
        """Return the number of cards in the Deck."""
        return len(self._cards)

    def isEmpty(self) -> bool:
        """Return True iff the deck is empty."""
        return len(self._cards) == 0

    # Mutator methods
    def deal(self) -> T:
        return self._cards.pop()
