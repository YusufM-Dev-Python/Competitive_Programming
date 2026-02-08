# Day 9: Lawnmower Problem (Codeforces Round 1050 - A)
# Logic: Simple Math. We subtract the number of multiples of 'w' 
# from the total 'n' to find the remaining units.
# Time Complexity: O(m) - where m is the number of test cases.
# Space Complexity: O(1) - minimal variable usage.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # m: Number of test cases
    try:
        line = input()
        if not line: return
        m = int(line)
    except ValueError:
        return

    for _ in range(m):
        # n: Total items, w: The periodic skip/constraint
        n, w = map(int, input().split())

        # The calculation: Total minus (Number of groups of size w)
        # This gives us the final count after the periodic removal.
        print(n - (n // w))

if __name__ == "__main__":
    solve()