# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import List

def fact(n:int) -> int:
    """Return the factorial of N."""
    # Pre:
    assert n > 0
    result:int = 1
    for i in range(1, n+1):
        result *= i
    return result

def main(args:List[str]) -> int:
    n:int = int(input('Please enter a number to take the factorial of: '))
    print('{0}! = {1}'.format(n, fact(n)))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))