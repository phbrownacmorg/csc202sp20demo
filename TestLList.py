#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  testLList.py: empty unit-testing class
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
from LList import LList
# Import the module(s) you want to test here

class TestNothing(unittest.TestCase):

    def setUp(self) -> None:
        """Run before every test."""
        self._list1 = LList()
        self._list1.add("foo")
        
        self._list2 = LList()
        self._list2._next = self._list1
        self._list2._data = 'bar'
        
    # Every function in this class whose name begins with 'test'
    # will be executed when the code is run
    def test_nothing(self) -> None:
        self.assertTrue((LList()).isEmpty())
        
    def testEmptyFalse(self) -> None:
        self.assertFalse(self._list1.isEmpty())

    def testStr(self) -> None:
        print(self._list1)
        print(self._list2)
        self.assertEqual(str(self._list1), "\u276cfoo\u276d\u279e\u2205")
        self.assertEqual(str(self._list2),
                         "\u276cbar\u276d\u279e\u276cfoo\u276d\u279e\u2205")
        
    def testSize(self) -> None:
        self.assertEqual((LList()).size(), 0)
        self.assertEqual(self._list1.size(), 1)
        self.assertEqual(self._list2.size(), 2)
        
    def testSearch(self) -> None:
        self.assertFalse((LList()).search('happiness'))
        self.assertFalse(self._list1.search('meaning'))
        self.assertFalse(self._list2.search('Spock'))
        self.assertTrue(self._list1.search('foo'))
        self.assertTrue(self._list2.search('bar'))
        self.assertTrue(self._list2.search('foo'))
        
    def testAdd(self) -> None:
        # Already did adding in setUp
        self.assertTrue(self._list2._invariant())
        self.assertTrue(self._list1._invariant())
        self.assertEqual(self._list2.size(), 2)
        self._list2.add('baz')
        self.assertEqual(self._list2.size(), 3)
        self.assertTrue(self._list2._invariant())
        
    def testPop1L1(self) -> None:
        self.assertEqual(self._list1.pop(), 'foo')
        self.assertTrue(self._list1.isEmpty())
        
    def testPop2L2(self) -> None:
        self.assertEqual(self._list2.pop(), 'foo')
        self.assertEqual(self._list2.size(), 1)
    
    def testPopNegL2(self) -> None:
        self.assertEqual(self._list2.pop(-2), 'bar')
        self.assertEqual(self._list2.size(), 1)

    def testPopPosL2(self) -> None:
        self.assertEqual(self._list2.pop(0), 'bar')
        self.assertEqual(self._list2.size(), 1)

    def testPopPos1L2(self) -> None:
        self.assertEqual(self._list2.pop(1), 'foo')
        self.assertEqual(self._list2.size(), 1)
        self.assertEqual(self._list2.pop(0), 'bar')
        self.assertEqual(self._list2.size(), 0)

    def testPop1L3(self) -> None:
        self._list2.add('baz')
        self.assertEqual(self._list2.pop(1), 'bar')
        self.assertEqual(self._list2.size(), 2)
        self.assertEqual(self._list2.pop(), 'foo')
        self.assertEqual(self._list2.size(), 1)
        self.assertEqual(self._list2.pop(), 'baz')
        self.assertEqual(self._list2.size(), 0)

if __name__ == '__main__':
    unittest.main()
