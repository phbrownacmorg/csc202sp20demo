#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  TestCard.py: unit tests for Card
#  
#  Copyright 2020 Peter Brown <peter.brown@converse.edu>
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

import unittest
from Card import Card
# Import the module(s) you want to test here

class TestCard(unittest.TestCase):

    def test_constructor(self) -> None:
        c:Card = Card('10', 'clubs') # Does it crash?
        self.assertTrue(True)

    def test_suit(self) -> None:
        self.assertEqual(Card('10', 'clubs').suit(), 'clubs')

    def test_rank(self) -> None:
        self.assertEqual(Card('10', 'clubs').rank(), '10')

    def test_str_10clubs(self) -> None:
        self.assertEqual(str(Card('10', 'clubs')), '10 of clubs')

    def test_str_Aspades(self) -> None:
        self.assertEqual(str(Card('A', 'spades')), 'A of spades')

    def test_str_Jdiamonds(self) -> None:
        self.assertEqual(str(Card('J', 'diamonds')), 'J of diamonds')

    def test_str_Qhearts(self) -> None:
        self.assertEqual(str(Card('Q', 'hearts')), 'Q of hearts')

    def test_str_Kclubs(self) -> None:
        self.assertEqual(str(Card('K', 'clubs')), 'K of clubs')
    
    def test_lt_yes_rank(self) -> None:
        self.assertTrue(Card('10', 'clubs') < Card('J', 'clubs'))

    def test_lt_no_rank(self) -> None:
        self.assertFalse(Card('J', 'clubs') < Card('10', 'clubs'))

    def test_lt_no_eq(self) -> None:
        self.assertFalse(Card('10', 'clubs') < Card('10', 'clubs'))

    def test_lt_yes_suit(self) -> None:
        self.assertTrue(Card('10', 'clubs') < Card('10', 'diamonds'))
    
    def test_lt_no_suit(self) -> None:
        self.assertFalse(Card('10', 'hearts') < Card('10', 'diamonds'))

    def test_lt_rank_vs_suit(self) -> None:
        self.assertFalse(Card('K', 'clubs') < Card('10', 'hearts'))

    def test_gt(self) -> None:
        self.assertTrue(Card('J', 'clubs') > Card('10', 'clubs'))

    # functools.total_ordering should allow this, but for some reason it doesn't
    def test_le(self) -> None:
        self.assertTrue(Card('10', 'clubs') <= Card('J', 'clubs')
                        and Card('10', 'clubs') <= Card('10', 'clubs'))

    def test_makeDeck(self) -> None:
        deck = Card.makeDeck()
        self.assertEqual(len(deck), 52)
        for i in range(len(deck)):
            self.assertEqual(deck[i].suit(), Card.SUITS[i // 13])
            self.assertEqual(deck[i].rank(), Card.RANKS[i % 13 + 1])

if __name__ == '__main__':
    unittest.main()
