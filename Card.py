# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import cast, List, Tuple
from AbstractCard import AbstractCard

class Card(AbstractCard):
    """Class to represent a stadnard French-style playing card.  A Card once created 
    is immutable."""

    # Assume aces low
    RANKS:Tuple[str, ...] = ('', 'A', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', 'J', 'Q', 'K')
    MIN_VAL:int = 1
    MAX_VAL:int = len(RANKS) - 1
    SUITS:Tuple[str, ...] = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, rank:str, suit:str) -> None:
        """Construct a Card with a given SUIT and rank."""
        super().__init__(rank, suit)

    # Query methods
    def __str__(self) -> str:
        return self.rank() + ' of ' + self.suit()

    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        deck:List[AbstractCard] = []
        for suit in Card.SUITS:
            for rank in Card.RANKS[1:]:
                deck.append(Card(rank, suit))
        # Post:
        assert len(deck) == 52
        return deck