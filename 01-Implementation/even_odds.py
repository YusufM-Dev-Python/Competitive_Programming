"""
Day 19: Even Odds (Codeforces 318A)
Problem Link: https://codeforces.com/contest/318/problem/A

Logic:
We are asked to find the k-th number in a sequence where all odd numbers 
from 1 to n come first, followed by all even numbers.
- Total odd numbers = (n + 1) // 2
- If k <= mid: The k-th number is the k-th odd number -> 2*k - 1
- If k > mid: The k-th number is the (k-mid)-th even number -> 2*(k - mid)

Complexity Analysis:
- Time: O(1) - Pure mathematical calculation.
- Space: O(1) - No data structures required.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input().split()
    if not line: return
    n, k = map(int, line)

    # Calculate how many odd numbers exist in the range [1, n]
    mid = (n + 1) // 2

    if k <= mid:
        # k is in the first half (odd numbers)
        print(2 * k - 1)
    else:
        # k is in the second half (even numbers)
        relative_pos = k - mid
        print(2 * relative_pos)

if __name__ == "__main__":
    solve()