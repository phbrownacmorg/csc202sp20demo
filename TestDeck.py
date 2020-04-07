#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  testnothing.py: empty unit-testing class
#  
#  Copyright 2018 Peter Brown <peter.brown@converse.edu>
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

from typing import cast, Iterable, List
import unittest
# Import the module(s) you want to test here
from AbstractCard import AbstractCard
from Deck import Deck
from Card import Card
from UnoCard import UnoCard

class TestDeck(unittest.TestCase):

    def test_Card(self) -> None:
        deck:Deck[Card] = Deck(cast(Iterable[Card], Card.makeDeck()))
        self.assertEqual(len(deck), 52)

    def test_UnoCard(self) -> None:
        deck:Deck[UnoCard] = Deck(cast(Iterable[UnoCard], UnoCard.makeDeck()))
        self.assertEqual(len(deck), 108)

    # Test dealing a single Card
    def testDealCard(self) -> None:
        deck:Deck[Card] = Deck(cast(Iterable[Card], Card.makeDeck()))
        self.assertEqual(deck.deal(), Card('K', 'spades'))
        self.assertEqual(len(deck), 51)

    def testDealEntireDeckCard(self) -> None:
        deck:Deck[Card] = Deck(cast(Iterable[Card], Card.makeDeck()))
        for i in range(51, -1, -1):
            card:Card = deck.deal()
            self.assertEqual(card.suit(), Card.SUITS[i // 13])
            self.assertEqual(card.rank(), Card.RANKS[i % 13 + 1])
        self.assertTrue(deck.isEmpty())

    def testPolymorphism(self) -> None:
        # Make a Deck with different types of cards in it
        mixed_list:List[AbstractCard] = []
        mixed_list.extend(Card.makeDeck())
        mixed_list.extend(UnoCard.makeDeck())
        mixed_deck = Deck[AbstractCard](mixed_list)
        self.assertEqual(len(mixed_deck), 108+52)

        # Run through the deck, printing out each card (which calls __str__())
        for i in range(len(mixed_deck)):
            # As far as *this* code knows, card is just an AbstractCard
            card:AbstractCard = mixed_deck.deal()
            # In calling __str__(), Python asks the *object itself* which __str__() method
            #     to call, and the object Does The Right Thing for the type of card that it
            #     really is
            print(card)

if __name__ == '__main__':
    unittest.main()
