#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  testNothing.py: empty unit-testing class
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

import unittest
# Import the module(s) you want to test here
from Card import Card

# All three implementation of the Queue class should pass exactly the same tests
# Pick ONLY ONE of the following three lines to uncomment
#from Queue import Queue
#from CircQ import Queue
from Q2Stacks import Queue

class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        """This function is executed before each test function."""
        self.st0 = Queue[Card]()
        
        self.H5 = Card('5', 'hearts')
        self.st1 = Queue[Card]()
        self.st1.push(self.H5)
        
        self.H6 = Card('6', 'hearts')
        self.H7 = Card('7', 'hearts')
        self.QH = Card('Q', 'hearts')
        self.AS = Card('A', 'spades')
        
        self.q4 = Queue[Card]()
        self.q4.push(self.H5)
        self.q4.push(self.H6)
        self.q4.push(self.H7)
        self.q4.push(self.QH)

    # Every function in this class whose name begins with 'test'
    # will be executed when the code is run
    def test_emptyTrue(self) -> None:
        self.assertTrue(self.st0.empty())

    def test_emptyFalse(self) -> None:
        self.assertFalse(self.st1.empty())
        
    def test_peek(self) -> None:
        self.assertEqual(self.st1.peek(), self.H5)
        self.assertFalse(self.st1.empty())

    def testPop1(self) -> None:
        self.assertEqual(self.st1.pop(), self.H5)
        self.assertTrue(self.st1.empty())
    
    def testPop2(self) -> None:
        st = Queue[Card]()
        jd = Card('J', 'diamonds')
        st.push(self.H5)
        st.push(jd)
        self.assertEqual(st.pop(), self.H5)
        self.assertEqual(st.pop(), jd)
        self.assertTrue(st.empty())
        
    def testCirc(self) -> None:
        self.assertEqual(self.q4.pop(), self.H5)
        self.assertEqual(self.q4.pop(), self.H6)
        self.q4.push(self.AS)
        self.q4.push(self.H5)
        self.assertEqual(self.q4.pop(), self.H7)
        self.assertEqual(self.q4.pop(), self.QH)
        self.assertEqual(self.q4.pop(), self.AS)
        self.assertEqual(self.q4.pop(), self.H5)
        self.assertTrue(self.q4.empty())
        
    def testResize(self) -> None:
        self.q4.push(self.AS)
        self.assertEqual(self.q4.pop(), self.H5)
        self.assertEqual(self.q4.pop(), self.H6)
        self.assertEqual(self.q4.pop(), self.H7)
        self.assertEqual(self.q4.pop(), self.QH)
        self.assertEqual(self.q4.pop(), self.AS)
        self.assertTrue(self.q4.empty())
        
if __name__ == '__main__':
    unittest.main()
