"""
Day 18: Odd Divisor (Codeforces 1475A)
Problem Link: https://codeforces.com/contest/1475/problem/A

Logic:
Any integer can be expressed as n = (2^k) * m, where 'm' is an odd number.
- If n is a power of 2, then m = 1 (no odd divisor > 1).
- If n is NOT a power of 2, then m > 1 (exists an odd divisor).

Bitwise Trick:
(n & (n - 1)) is a famous trick to remove the rightmost set bit.
If (n & (n - 1)) == 0, the number had only one set bit, meaning it's a power of 2.

Complexity Analysis:
- Time: O(1) per test case - Bitwise operations are near-instant.
- Space: O(1) - No extra storage used.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())

        # Check if n is a power of 2 using bitwise AND
        # If n is a power of 2, it has no odd divisors > 1.
        if (n & (n - 1)) == 0:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve()