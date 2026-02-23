"""
Day 22: Promo (Codeforces 1697B)
Problem Link: https://codeforces.com/contest/1697/problem/B

Logic:
1. To maximize the discount, we pick the X most expensive items.
2. The discount gives us the Y cheapest items among those X.
3. Sorting descending: The X most expensive are at the start of the array.
4. The Y cheapest among those X are the items from index (X-Y) to (X-1).
5. We use a prefix sum array to answer these range sum queries in O(1).

Complexity Analysis:
- Time: O(N log N + Q) - Sorting takes O(N log N), prefix sums take O(N), 
  and queries take O(Q).
- Space: O(N) - To store the prefix sum array.
"""

import sys

# Faster I/O is necessary for 2*10^5 queries
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of items, q: number of queries
    line1 = input().split()
    if not line1: return
    n, q = map(int, line1)

    # Prices of items
    arr = list(map(int, input().split()))

    # Sort prices descending to pick most expensive items first
    arr.sort(reverse=True)

    # Precompute Prefix Sum array
    p = [0] * (n + 1)
    for i in range(n):
        p[i+1] = p[i] + arr[i]

    # Process each query
    for _ in range(q):
        x, y = map(int, input().split())
        
        # We need the sum of the last Y items in the first X items.
        # This range in the sorted list is [x-y, x-1].
        # Using prefix sum: p[x] - p[x-y]
        print(p[x] - p[x-y])

if __name__ == "__main__":
    solve()