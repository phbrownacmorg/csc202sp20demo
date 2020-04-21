#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  recursive_sum_list.py
#  
#  Copyright 2019, 2020 phbrown <phbrown@KUH-212-CLPC>
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
#  

from typing import List

# Recursive definition for string reversal:
#   The reverse of a string STRVAL, strRev(strval), is:
#      If STRVAL is empty: strRev(strval) = strval
#      If STRVAL only has a single character: strRev(strval) = strval
#      If STRVAL has more than one character, then
#        swap the first and last characters and reverse whatever's between them
def strRev(strval:str) -> str:
    """Reverse a string STRVAL.  Return the reversed string."""
    print("Calling strRev('{0}')".format(strval))
    if len(strval) < 2: # Base case
        result = strval
    else:                  # Recursive case
        result = strval[-1] + strRev(strval[1:-1]) + strval[0]
    
    print("strRev('{0}') returning '{1}'".format(strval, result))
    return result

# Recursive definition of GCD of two numbers A and B:
#  If B == 0: GCD = |A|  (use the absolute value so it handles negative numbers)
#  If B != 0: GCD(A, B) = GCD(B, A % B)  (Euclid proved this)
def gcd(a:int, b:int) -> int:
    """Find and return the GCD of two integers A and B."""
    print("Calling gcd({0}, {1})".format(a, b))
    if b == 0: # Base case
        result = abs(a)
    else:
        result = gcd(b, a % b)
    print("gcd({0}, {1}) returning {2}".format(a, b, result))
    return result

# Recursive definition of A**B
# If B == 0:  A**B = 1               Base case
# If B > 0:   A**B = A * A**(B-1)    Recursive case
def expt(a:float, b:int) -> float:
    """Find and return A ** B, recursively.  This requires that
    B is a non-negative integer."""
    # Pre:
    assert b >= 0
    print("Calling expt({0}, {1})".format(a, b))
    if b == 0: # Base case
        result:float = 1
    else:      # Recursive case
        result = a * expt(a, b-1)
    print("expt({0}, {1}) returning {2}".format(a, b, result))
    return result

# Recursive definition of A**B that executes faster
# If B == 0:              A**B = 1               Same base case as above
# If B > 0 and B is even: A**B = (A**(B//2))**2  Raising exponents to a power
# If B > 0 and B is odd:  A**B = A * (A**(B//2))**2
def fastexpt(a:float, b:int) -> float:
    """Find and return A ** B, recursively.  This requires that
    B is a non-negative integer."""
    print("Calling fastexpt({0}, {1})".format(a, b))
    if b == 0: # Base case
        result:float = 1
    else:      # Recursive case(s)
        halfexpt = fastexpt(a, b // 2)
        result = halfexpt * halfexpt # Works for even b
        if (b % 2) != 0: # Odd b
            result = a * result
    print("fastexpt({0}, {1}) returning {2}".format(a, b, result))
    return result

# If you run this file, you will see the pattern of recursive calls printed out
def main(args:List[str]) -> int:
    print(strRev('') == '', '\n')
    print(strRev('q') == 'q', '\n')
    print(strRev('ab') == 'ba', '\n')
    print(strRev('abc') == 'cba', '\n')
    print(strRev('abcd') == 'dcba', '\n')

    print(gcd(3, 3) == 3, '\n')
    print(gcd(9, 12) == 3, '\n')
    print(gcd(-6, 4) == 2, '\n')
    print(gcd(243, -108) == 27, '\n')
    print(gcd(-24, -36) == 12, '\n')
    
    print(expt(2, 0) == 1, '\n')
    print(expt(-2, 1) == -2, '\n')
    print(expt(2, 8) == 256, '\n')
    
    print(fastexpt(2, 0) == 1, '\n')
    print(fastexpt(-2, 1) == -2, '\n')
    print(fastexpt(2, 8) == 256, '\n')
    print(fastexpt(2, 15) == 32768, '\n')
    print(fastexpt(2, 16) == 65536, '\n')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
