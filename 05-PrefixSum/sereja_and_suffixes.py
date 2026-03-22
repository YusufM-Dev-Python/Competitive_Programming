"""
Day 36: Sereja and Suffixes (Codeforces 368B)
Problem Link: https://codeforces.com/contest/368/problem/B

Logic:
1. The problem asks for the number of distinct integers from index L to N.
2. Brute force for each query is too slow.
3. We precompute a suffix array 'dp' where dp[i] is the number of distinct
   elements in the range [i, n-1].
4. We iterate from the back of the array to the front, adding elements to 
   a set and storing the set's size in dp[i].

Complexity Analysis:
- Time: O(N + M) - O(N) to build the suffix counts, O(M) to answer queries.
- Space: O(N) - To store the dp array and the set of seen elements.
"""

import sys

# Faster I/O is mandatory for 10^5 queries
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: array size, m: number of queries
    line1 = input().split()
    if not line1: return
    n, m = map(int, line1)

    arr = list(map(int, input().split()))

    # dp[i] will store the number of distinct elements from i to n-1
    seen = set()
    dp = [0] * n
    
    # Traverse from right to left (Suffix approach)
    for i in range(n - 1, -1, -1):
        seen.add(arr[i])
        dp[i] = len(seen)

    # Answer each query in O(1)
    for _ in range(m):
        l = int(input())
        # The input 'l' is 1-based, so we access dp[l-1]
        print(dp[l - 1])

if __name__ == "__main__":
    solve()