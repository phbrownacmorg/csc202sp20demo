# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import List
# import the code to time
import factorial
import math
import timeit

def main(args:List[str]) -> int:
    t:timeit.Timer = timeit.Timer(stmt='factorial.fact(1)', setup='import factorial')
    # print(t.autorange())
    #print(min(t.repeat(number=1000)))

    # Analytically, factorial.fact() should be O(n)
    # Empirically:
    # t(fact(1)) ~= 0.0004
    # t(fact(10)) ~= 0.0008
    # t(fact(100)) ~= 0.007
    # t(fact(1000)) ~= 0.27
    # t(fact(10000)) ~= 21.5
    #
    # That's more than O(n), but not by a whole lot--in particular, not by enough to suggest
    # O(n log n).

    t = timeit.Timer(stmt='math.factorial(10000)', setup='import math')
    # print(min(t.repeat(number=1000)))
    # Empirically:
    # t(math.factorial(1)) ~= 0.00006
    # t(math.factorial(10)) ~= 0.00007
    # t(math.factorial(100)) ~= 0.0014
    # t(math.factorial(1000)) ~= 0.049
    # t(math.factorial(10000)) ~= 3.02
    #
    # Again, that's higher than O(n), but not by a lot.

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))

# Computer:
# CPU: Intel Core i5-6500 @ 3.2 GHz
# OS: WIndows 10 Enterprise version 1709 build 16299.1686
# Python version 3.7.2