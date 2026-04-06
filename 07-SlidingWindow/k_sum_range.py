"""
Day 49: Sum of k Distinct Elements (Codeforces 1899A Variant)
Problem Link: https://codeforces.com/contest/1899/problem/A

Logic:
1. We need to choose k distinct integers from 1 to n that sum to x.
2. The smallest possible sum is the sum of the first k integers:
   min_sum = 1 + 2 + ... + k = k * (k + 1) // 2
3. The largest possible sum is the sum of the last k integers:
   max_sum = (n-k+1) + ... + n = k * (2*n - k + 1) // 2
4. If x is within [min_sum, max_sum], the sum is achievable.

Complexity Analysis:
- Time: O(T) - Constant time calculations per test case.
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
        line = input().split()
        if not line: continue
        n, k, x = map(int, line)
        
        # Sum of first k elements: 1, 2, ..., k
        min_sum = k * (k + 1) // 2
        
        # Sum of last k elements: (n-k+1), ..., n
        # Formula: (k / 2) * (first_term + last_term)
        max_sum = k * (2 * n - k + 1) // 2

        if min_sum <= x <= max_sum:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()