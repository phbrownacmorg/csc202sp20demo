#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  TestStack.py: unit tests for Stack class
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
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack:Stack[str] = Stack[str]()

    def test_empty(self) -> None:
        self.assertTrue(self.stack.empty())

    def testPushPeek(self) -> None:
        self.assertTrue(self.stack.empty()) # Starts out empty
        self.stack.push("Humpty Dumpty")
        self.assertFalse(self.stack.empty()) # Now not empty
        self.assertEqual(self.stack.peek(), "Humpty Dumpty") # Correct object on top

    def testPop(self) -> None:
        self.assertTrue(self.stack.empty()) # Starts out empty
        self.stack.push("Humpty Dumpty")
        self.assertFalse(self.stack.empty()) # Now not empty
        self.assertEqual(self.stack.pop(), "Humpty Dumpty")
        self.assertTrue(self.stack.empty()) # Empty again

    def testLIFO(self) -> None:
        self.assertTrue(self.stack.empty()) # Starts out empty
        self.stack.push("Humpty Dumpty")
        self.assertFalse(self.stack.empty()) # Now not empty
        self.stack.push("grape")
        self.assertFalse(self.stack.empty()) # Still not empty
        self.assertEqual(self.stack.pop(), 'grape')
        self.assertFalse(self.stack.empty()) # Still not empty
        self.assertEqual(self.stack.pop(), "Humpty Dumpty")
        self.assertTrue(self.stack.empty()) # Empty again


if __name__ == '__main__':
    unittest.main()
