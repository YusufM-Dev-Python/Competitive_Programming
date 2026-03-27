"""
Day 41: Three Parts of the Array (Codeforces 1006C)
Problem Link: https://codeforces.com/contest/1006/problem/C

Logic:
1. Use two pointers, 'l' starting at the beginning and 'r' at the end.
2. Maintain 'sum_l' (sum of the prefix) and 'sum_r' (sum of the suffix).
3. If sum_l < sum_r, increment 'l' to increase sum_l.
4. If sum_r < sum_l, decrement 'r' to increase sum_r.
5. If sum_l == sum_r, update max_sum and move 'l' (or 'r') forward.
6. The loop stops when the pointers meet (l >= r).

Complexity Analysis:
- Time: O(N) - Single pass through the array.
- Space: O(N) - To store the array.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input()
    if not line1: return
    n = int(line1)
    d = list(map(int, input().split()))

    l = 0
    r = n - 1
    max_balanced_sum = 0

    # Initialize sums with the first and last elements
    sum_l = d[l]
    sum_r = d[r]

    # Converging pointers logic
    while l < r:
        if sum_l == sum_r:
            # Found a valid split where prefix sum equals suffix sum
            max_balanced_sum = sum_l
            # Move l forward to look for a larger balanced sum
            l += 1
            sum_l += d[l]
        elif sum_l < sum_r:
            l += 1
            sum_l += d[l]
        else: # sum_r < sum_l
            r -= 1
            sum_r += d[r]
        
    print(max_balanced_sum)

if __name__ == "__main__":
    solve()