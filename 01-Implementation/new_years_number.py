"""
Day 27: New Year's Number (Codeforces 1475B)
Problem Link: https://codeforces.com/contest/1475/problem/B

Logic:
We need to check if n = 2020 * x + 2021 * y for some non-negative x, y.
Since 2021 = 2020 + 1, we can rewrite this as:
n = 2020 * x + (2020 + 1) * y
n = 2020 * (x + y) + y

Let total_2020s = x + y.
Then n // 2020 gives us the maximum number of 2020s (x + y).
The remainder n % 2020 gives us the required value for 'y'.
If y <= total_2020s, then a valid non-negative x exists.

Complexity Analysis:
- Time: O(1) per test case.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input()
    if not line: return
    t = int(line)

    for _ in range(t):
        n = int(input())

        # How many 2020s can we fit in n?
        count = n // 2020
        # What is left over?
        rem = n % 2020

        # Each '1' in the remainder requires one 2020 to be changed to 2021.
        # So we need at least as many total 2020s as the remainder.
        if rem <= count:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()