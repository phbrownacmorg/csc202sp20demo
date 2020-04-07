# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import List
from Stack import Stack

def base_convert(n:int, base:int) -> str:
    digits:str = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Precondition
    assert n > 0 and 1 < base <= len(digits)
    stack:Stack[str] = Stack[str]()

    quotient:int = n
    while quotient > 0: # Repeated division to generate the digits, least significant first
        stack.push(digits[quotient % base])
        quotient = quotient // base
    
    result = ''
    while not stack.empty(): # Retrieve the digits
        result = result + stack.pop()
    return result
    
def main(args:List[str]) -> int:
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))