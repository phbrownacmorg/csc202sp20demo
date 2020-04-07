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


import unittest
# Import the module(s) you want to test here
from delimiters import matched_delims

class TestDelims(unittest.TestCase):

    def test_empty(self) -> None:
        self.assertTrue(matched_delims(''))

    def testLPar(self) -> None:
        self.assertFalse(matched_delims('('))

    def test1Char0Delims(self) -> None:
        self.assertTrue(matched_delims('y'))

    def testPairs(self) -> None:
        self.assertTrue(matched_delims('()[]{}'))

    def testStackUnderflow(self) -> None:
        self.assertFalse(matched_delims('())('))

    def testDeep(self) -> None:
        self.assertTrue(matched_delims('([{ ([{ ([{}]) }]) }])'))


if __name__ == '__main__':
    unittest.main()
