"""
Day 24: K-th Not Divisible by n (Codeforces 1374C)
Problem Link: https://codeforces.com/contest/1374/problem/C

Logic:
We need the k-th integer that is NOT divisible by n.
- In every group of 'n' consecutive integers, there are (n-1) integers
  not divisible by n.
- Example: n=3. Numbers: 1, 2, (3), 4, 5, (6), 7, 8...
  Non-divisibles are in pairs (1,2), (4,5), (7,8).
- We find how many full blocks of (n-1) fit into k.
- 'blocks' tells us how many multiples of n we have skipped.

Complexity Analysis:
- Time: O(1) per test case - Pure mathematical calculation.
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
        n, k = map(int, input().split())
        
        # Calculate how many full groups of (n-1) non-divisibles exist
        blocks = k // (n - 1)
        rem = k % (n - 1)

        if rem == 0:
            # If k is a multiple of n-1, we are at the end of a block
            # The result is the blocks-th multiple of n, minus 1.
            print(blocks * n - 1)
        else:
            # Otherwise, we skip 'blocks' multiples of n and add the remainder
            print(blocks * n + rem)

if __name__ == "__main__":
    solve()