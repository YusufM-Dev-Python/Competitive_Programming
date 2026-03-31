"""
Day 45: Worms (Codeforces 474B)
Problem Link: https://codeforces.com/contest/474/problem/B

Logic:
1. Piles of worms form continuous ranges. 
2. Create a prefix sum array where prefix_sum[i] is the total number 
   of worms in the first 'i' piles.
3. This creates a sorted array of the end-boundaries of each pile.
4. For each juicy worm 'target', use Binary Search to find the 
   smallest index 'i' such that prefix_sum[i] >= target.

Complexity Analysis:
- Time: O(N + M log N) - O(N) to build prefix sum, O(M log N) for queries.
- Space: O(N) - To store the prefix sums.
"""

import sys

# Faster I/O for 10^5 inputs
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_str = input()
    if not n_str: return
    n = int(n_str)
    worms = list(map(int, input().split()))
    
    m_str = input()
    if not m_str: return
    m = int(m_str)
    juicy = list(map(int, input().split()))

    # Build Prefix Sum: 1-based indexing for piles
    # prefix_sum[i] = total worms from pile 1 to pile i
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + worms[i]

    # Binary Search for each query
    for target in juicy:
        l = 1
        r = n
        ans = 1
        
        while l <= r:
            mid = (l + r) // 2
            # If the end of this pile is >= target, it's a candidate
            if prefix_sum[mid] >= target:
                ans = mid 
                r = mid - 1 # Try to find an even smaller pile index
            else:
                l = mid + 1 # Target must be in a later pile
        print(ans)

if __name__ == "__main__":
    solve()