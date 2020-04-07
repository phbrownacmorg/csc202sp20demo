#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  testUnoCard.py: unit tests for UnoCard
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
# Import the module(s) you want to test here
from UnoCard import UnoCard
from typing import List

class TestUnoCard(unittest.TestCase):

    def test_constructor(self) -> None:
        c:UnoCard = UnoCard('8', 'Red')     # Does it crash?
        c = UnoCard('Skip', 'Blue')
        c = UnoCard('Draw Two', 'Yellow')
        c = UnoCard('0', 'Green')
        c = UnoCard('Draw Four', 'Wild')
        c = UnoCard('', 'Wild')
        self.assertTrue(True)

    def test_color_ranks(self) -> None:
        for rank in UnoCard.COLOR_RANKS:
            self.assertEqual(UnoCard(rank, 'Green').rank(), rank)
            
    def test_wild_ranks(self) -> None:
        for rank in UnoCard.WILD_RANKS:
            self.assertEqual(UnoCard(rank, 'Wild').rank(), rank)
            
    def test_color_suits(self) -> None:
        for suit in UnoCard.COLOR_SUITS:
            self.assertEqual(UnoCard('Draw Two', suit).suit(), suit)

    def test_wild_suit(self) -> None:
        self.assertEqual(UnoCard('', 'Wild').suit(), 'Wild')

    def test_color_str_num(self) -> None:
        self.assertEqual(str(UnoCard('8', 'Blue')), 'Blue 8')

    def test_color_str_name(self) -> None:
        self.assertEqual(str(UnoCard('Reverse', 'Red')), 'Red Reverse')

    def test_str_wild_draw4(self) -> None:
        self.assertEqual(str(UnoCard('Draw Four', 'Wild')), 'Wild Draw Four')

    def test_str_wild(self) -> None:
        self.assertEqual(str(UnoCard('', 'Wild')), 'Wild')

    def test_eq_yes(self) -> None:
        self.assertEqual(UnoCard('3', 'Yellow'), UnoCard('3', 'Yellow'))

    def test_eq_no_rank(self) -> None:
        self.assertNotEqual(UnoCard('3', 'Yellow'), UnoCard('6', 'Yellow'))

    def test_eq_no_suit(self) -> None:
        self.assertNotEqual(UnoCard('3', 'Yellow'), UnoCard('3', 'Blue'))

    def test_eq_no_both(self) -> None:
        self.assertNotEqual(UnoCard('3', 'Yellow'), UnoCard('6', 'Blue'))

    def test_lt_yes_rank(self) -> None:
        self.assertTrue(UnoCard('7', 'Blue') < UnoCard('Skip', 'Blue'))

    def test_lt_no_rank(self) -> None:
        self.assertFalse(UnoCard('7', 'Blue') > UnoCard('Skip', 'Blue'))

    def test_lt_no_eq(self) -> None:
        self.assertFalse(UnoCard('7', 'Blue') < UnoCard('7', 'Blue'))

    def test_lt_yes_suit(self) -> None:
        self.assertTrue(UnoCard('7', 'Blue') < UnoCard('7', 'Green'))
    
    def test_lt_no_suit(self) -> None:
        self.assertFalse(UnoCard('7', 'Yellow') < UnoCard('7', 'Green'))

    def test_lt_rank_vs_suit(self) -> None:
        self.assertFalse(UnoCard('Draw Two', 'Blue') < UnoCard('7', 'Yellow'))

    def test_lt_yes_wild(self) -> None:
        self.assertTrue(UnoCard('Draw Two', 'Yellow') < UnoCard('Draw Four', 'Wild'))

    def test_lt_no_wild(self) -> None:
        self.assertFalse(UnoCard('Draw Four', 'Wild') < UnoCard('Draw Two', 'Yellow'))

    def test_makeDeck(self) -> None:
        deck = UnoCard.makeDeck()
        self.assertTrue(len(deck) == 108)
        # zeroes
        for i in range(4):
            self.assertTrue(deck[i].rank() == '0')
            self.assertTrue(deck[i].suit() == UnoCard.COLOR_SUITS[i])
        # Other color ranks
        for i in range(4, 100):
            self.assertTrue(deck[i].rank() == UnoCard.COLOR_RANKS[((i-4) // 8) + 1])
            self.assertTrue(deck[i].suit() == UnoCard.COLOR_SUITS[i % 4])
        # Wild ranks
        for i in range(100, 104):
            self.assertTrue(deck[i].rank() == 'Draw Four')
            self.assertTrue(deck[i].suit() == 'Wild')
        for i in range(104, 108):
            self.assertTrue(deck[i].rank() == '')
            self.assertTrue(deck[i].suit() == 'Wild')


if __name__ == '__main__':
    unittest.main()
