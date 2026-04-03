"""
Day 46: Polycarp and Coins (Codeforces 1551A)
Problem Link: https://codeforces.com/contest/1551/problem/A

Logic:
1. Total value n = c1 + 2*c2.
2. We want c1 and c2 to be as close as possible.
3. Divide n by 3 to get the base count for both.
4. Use the remainder (n % 3) to decide which count to increment by 1.

Complexity Analysis:
- Time: O(T) where T is the number of test cases.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)

        base = n // 3
        rem = n % 3

        if rem == 0:
            print(f"{base} {base}")
        elif rem == 1:
            print(f"{base + 1} {base}")
        else: # rem == 2
            print(f"{base} {base + 1}")

if __name__ == "__main__":
    solve()