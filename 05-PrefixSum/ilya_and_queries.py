"""
Day 35: Ilya and Queries (Codeforces 313B)
Problem Link: https://codeforces.com/contest/313/problem/B

Logic:
1. We need to answer many queries about the number of indices i in [l, r-1]
   where s[i] == s[i+1].
2. Brute force is O(N*M), which is too slow.
3. We precompute a prefix sum array 'dp':
   - dp[i] = number of matching adjacent pairs in the prefix s[0...i].
4. For each query (l, r), the number of matches is dp[r-1] - dp[l-1].

Complexity Analysis:
- Time: O(N + M) - O(N) to build the prefix sum, O(M) to answer queries.
- Space: O(N) - To store the prefix sum array.
"""

import sys

# Faster I/O is critical when M = 10^5
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s = input()
    if not s: return
    n = len(s)
    
    # Precompute the prefix sums
    # dp[i] will store the count of j < i such that s[j] == s[j+1]
    dp = [0] * n
    
    for i in range(n - 1):
        # If the current character matches the next, increment the count
        if s[i] == s[i+1]:
            dp[i+1] = dp[i] + 1
        else:
            dp[i+1] = dp[i]
            
    m_str = input()
    if not m_str: return
    m = int(m_str)

    # Answer queries in O(1) each
    for _ in range(m):
        l, r = map(int, input().split())
        # The number of matches in range [l, r] is matches up to r-1 
        # minus matches up to l-1.
        print(dp[r-1] - dp[l-1])

if __name__ == "__main__":
    solve()