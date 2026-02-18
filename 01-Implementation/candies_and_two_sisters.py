"""
Day 18: Candies and Two Sisters (Codeforces 1335A)
Problem Link: https://codeforces.com/contest/1335/problem/A

Logic:
Two sisters, Alice (a) and Betty (b), share n candies.
Constraints: a > b, a + b = n, a > 0, b > 0.
This means b can be any integer from 1 up to (n-1)//2.
Example:
n = 7: b can be 1, 2, 3 (a would be 6, 5, 4). Total = 3.
n = 6: b can be 1, 2 (a would be 5, 4). Total = 2.

The formula (n-1) // 2 covers both scenarios perfectly.

Complexity Analysis:
- Time: O(1) per test case.
- Space: O(1).
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

        # O(1) math solution to find the number of ways a > b
        print((n - 1) // 2)

if __name__ == "__main__":
    solve()