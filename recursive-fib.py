# Do nothing, successfully
# Peter Brown, 2020-01-07


from typing import List, Tuple


def fib(n:int) -> int:
    """Calculate and return the N'th Fibonacci number, recursively.  The recursive defition is:
    fib(n) = n if n < 2 (base case)
           = fib(n-1) + fib(n-2) (recursive case)
    The resulting sequence will be 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    
    This function is coded straight from the definition of the Fibonacci sequence.  It works,
    but it's slow for large values of n (as in, over about 35).  The problem is that with two
    calls to fib() in the recursive case, the total number of function calls is O(2**n)."""
    # Pre:
    assert n >= 0
    result:int = 0 # Bogus value, just to have a value there
    if n < 2: # Base case
        result = n
    else: # Recursive case
        result = fib(n - 1) + fib(n - 2)
    return result

def fastfib(n:int) -> Tuple[int, int]:
    """Calculate and return a tuple with the N'th and (N-1)'th Fibonacci numbers.  This allows
    the Fibonacci sequence to be calculated fast even for large N, because there's only one
    recursive call each time."""
    # Pre:
    assert n >= 0
    result:Tuple[int, int] = (0, 0)
    if n < 2:
        result = (n, 0)
    else:
        prev:Tuple[int, int] = fastfib(n - 1) # Note only one recursive call, which returns both fib(n-1) and fib(n-2)
        result = (prev[0] + prev[1], prev[0]) # Wrap up fib(n) and fib(n - 1) in a tuple, and return them

    return result


def main(args:List[str]) -> int:
    for i in range(35):
        print(i, '\t', fib(i))
    for i in range(350):
        print(i, '\t', fastfib(i)[0])
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))