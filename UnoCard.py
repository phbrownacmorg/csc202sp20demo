# Class to represent an Uno card
# Peter Brown, 2020-02-18

from typing import cast, List, Tuple
# import superclass
from AbstractCard import AbstractCard

class UnoCard(AbstractCard):
    """Class to represent an Uno card."""
    COLOR_RANKS:Tuple[str, ...] = ('0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two')
    WILD_RANKS:Tuple[str, str] = ('Draw Four', '')
    RANKS:Tuple[str, ...] = COLOR_RANKS + WILD_RANKS
    MIN_VAL:int = 0
    MAX_COLOR_VAL:int = len(COLOR_RANKS) - 1
    MAX_VAL:int = len(RANKS) - 1
    COLOR_SUITS:Tuple[str, ...] = ('Blue', 'Green', 'Red', 'Yellow')
    WILD_SUITS:Tuple[str] = ('Wild',)
    SUITS:Tuple[str, ...] = COLOR_SUITS + WILD_SUITS

    # Needs to be overridden, because the class invariant for an Uno card is more 
    #   restrictive than the class invariant for an AbstractCard.
    def _invariant(self) -> bool:
        valid_color:bool = self._suit in self.COLOR_SUITS and \
            (self.MIN_VAL <= self._rank <= self.MAX_COLOR_VAL)
        valid_wild:bool = self._suit == 'Wild' and \
            self.MAX_COLOR_VAL < self._rank <= self.MAX_VAL
        return valid_color or valid_wild

    def __init__(self, rank:str, suit:str) -> None:
        # Just call the Card constructor
        super().__init__(rank, suit)

    # rank() and suit() can be inherited from AbstractCard

    def __str__(self) -> str:
        return (self.suit() + ' ' + self.rank()).rstrip()

    # __eq__ and __lt__ are inherited from AbstractCard

    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        deck:List[AbstractCard] = []

        # Do the zeroes
        for suit in UnoCard.COLOR_SUITS:
            deck.append(UnoCard('0', suit))
        
        # Do the other color ranks
        for rank in UnoCard.COLOR_RANKS[1:]:
            for i in range(2):
                for suit in UnoCard.COLOR_SUITS:
                    deck.append(UnoCard(rank, suit))

        # Do the wild ranks
        for rank in UnoCard.WILD_RANKS:
            for i in range(4):
                deck.append(UnoCard(rank, 'Wild'))
        
        return deck