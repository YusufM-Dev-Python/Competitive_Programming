"""
Day 49: Money Trees (Codeforces 1873F)
Problem Link: https://codeforces.com/contest/1873/problem/F

Logic:
1. We need to find the longest subarray [l, r] such that:
   a) For all i from l to r-1, h[i] is divisible by h[i+1].
   b) The sum of fruits a[l...r] <= k.
2. We use a Sliding Window (Two Pointers):
   - If the divisibility rule is broken at 'r', reset the window to start at 'r'.
   - Add a[r] to curr_sum.
   - If curr_sum > k, shrink from the left until curr_sum <= k.
3. Keep track of the maximum window size (r - l + 1).

Complexity Analysis:
- Time: O(N) per test case - Each pointer moves from 0 to N once.
- Space: O(N) - To store the heights and fruits.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        h = list(map(int, input().split()))

        l = 0
        max_len = 0
        curr_sum = 0

        # Expand the right pointer
        for r in range(n):
            # Constraint 1: Divisibility rule
            # If broken, the subarray MUST restart at r
            if r > 0 and h[r-1] % h[r] != 0:
                curr_sum = 0
                l = r
            
            curr_sum += a[r]
        
            # Constraint 2: Sum limit k
            # Shrink from left if sum is too large
            while curr_sum > k and l <= r:
                curr_sum -= a[l]
                l += 1
            
            # Update the longest valid window found so far
            if curr_sum <= k:
                max_len = max(max_len, r - l + 1)

        print(max_len)

if __name__ == "__main__":
    solve()