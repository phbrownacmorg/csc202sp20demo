# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import List, Tuple
from Stack import Stack

def matched_delims(s:str) -> bool:
    "Takes a string S and returns True if and only if the delimiters in S are balanced."
    start_delims:Tuple[str, ...] = ('(', '[', '{') # Sticking to single-character delimiters
    end_delims:Tuple[str, ...] = (')', ']', '}')
    stack:Stack[str] = Stack[str]()
    balanced:bool = True

    for c in s:
        if c in start_delims:
            stack.push(end_delims[start_delims.index(c)])
        elif c in end_delims:
            balanced = balanced and (not stack.empty()) and c == stack.pop()
        if not balanced:
            break

    balanced = balanced and stack.empty()
    return balanced


def main(args:List[str]) -> int:
    s:str = input('Please enter a string to balance: ')
    print('The string "{0}" is'.format(s), end=' ')
    if not matched_delims(s):
        print('NOT', end=' ')
    print('balanced.')
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))