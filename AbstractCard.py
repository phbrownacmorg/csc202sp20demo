# Do nothing, successfully
# Peter Brown, 2020-01-07

from abc import ABCMeta, abstractmethod
from typing import cast, List, Tuple
import functools

class AbstractCard(metaclass=ABCMeta):
    """Abstract class to represent a playing card with a rank and suit.  A Card once created 
    is immutable."""

    # Python doesn't actually enforce abstract classes, except by convention.  You *can*,
    # however, set things up so that the class invariant fails unless something's overridden.
    RANKS:Tuple[str, ...] = ()
    MIN_VAL:int = 0
    MAX_VAL:int = len(RANKS) - 1
    SUITS:Tuple[str, ...] = ()

    def _invariant(self) -> bool:
        """Class invariant."""
        return self.MIN_VAL <= self._rank <= self.MAX_VAL \
            and self._suit in self.SUITS

    def __init__(self, rank:str, suit:str) -> None:
        """Construct a Card with a given SUIT and rank."""
        # Pre:
        assert rank in self.RANKS[self.MIN_VAL:self.MAX_VAL+1] \
            and suit in self.SUITS
        self._rank = self.RANKS.index(rank)
        self._suit = suit
        # Post:
        assert self._invariant()

    # Query methods
    def rank(self) -> str:
        return self.RANKS[self._rank]

    def suit(self) -> str:
        return self._suit

    @abstractmethod
    def __str__(self) -> str:
        return '' # Bogus value.  This method is here to be overridden.

    def __eq__(self, other:object) -> bool:
        same:bool = isinstance(other, AbstractCard)
        if same: # other is a Card
            othercard:AbstractCard = cast(AbstractCard, other)
            same = (self._rank == othercard._rank and 
                    self._suit == othercard._suit)
        return same
    
    def __lt__(self, other:object) -> bool:
        if not isinstance(other, AbstractCard):
            return NotImplemented
        else: 
            othercard:AbstractCard = other
            return self._rank < othercard._rank or \
               (self._rank == othercard._rank and self._suit < othercard._suit)

    # Other comparison methods built on the first two
    def __ne__(self, other:object) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other:object) -> bool:
        return not self.__lt__(other)

    def __le__(self, other:object) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other:object) -> bool:
        return (not self.__lt__(other)) and (not self.__eq__(other))
         
    @staticmethod
    @abstractmethod
    def makeDeck(): # type () -> List[AbstractCard]:
        deck:List[AbstractCard] = []
        return deck
