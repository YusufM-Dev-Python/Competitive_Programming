"""
Day 64: Minimum Product (Codeforces 1409B)
Logic:
1. We want to minimize a * b by decreasing a and b a total of n times.
2. Constraints: a cannot go below x, and b cannot go below y.
3. Strategy: It is always optimal to decrease one number as much as 
   possible before starting on the other.
4. Since we don't know which one to start with, we calculate both 
   scenarios (Decrease a then b, and Decrease b then a) and pick the min.

Complexity Analysis:
- Time: O(1) per test case.
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
        a, b, x, y, n = map(int, input().split())

        # Path 1: Focus on decreasing 'a' first
        # How much can we take from a?
        dec_a = min(n, a - x)
        rem_n1 = n - dec_a
        final_a1 = a - dec_a
        # Use remaining n on b
        dec_b1 = min(rem_n1, b - y)
        final_b1 = b - dec_b1
        res1 = final_a1 * final_b1

        # Path 2: Focus on decreasing 'b' first
        # How much can we take from b?
        dec_b = min(n, b - y)
        rem_n2 = n - dec_b
        final_b2 = b - dec_b
        # Use remaining n on a
        dec_a2 = min(rem_n2, a - x)
        final_a2 = a - dec_a2
        res2 = final_a2 * final_b2

        print(min(res1, res2))

if __name__ == "__main__":
    solve()