"""
Day 22: Kuriyama Mirai's Stones (Codeforces 433B)
Problem Link: https://codeforces.com/contest/433/problem/B

Logic:
1. Type 1 Query: Sum of elements in the original array from index l to r.
2. Type 2 Query: Sum of elements in the sorted array from index l to r.
We use Prefix Sums to answer these range queries in O(1) time.
- p1 stores the prefix sums of the original array.
- p2 stores the prefix sums of the sorted array.

Complexity Analysis:
- Time: O(N log N + M) - O(N log N) for sorting, O(N) to build prefix sums, 
  and O(M) to answer M queries.
- Space: O(N) - To store the two prefix sum arrays.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Number of stones
    line1 = input()
    if not line1: return
    n = int(line1)
    
    # Original stone costs
    arr = list(map(int, input().split()))
    
    # Sorted stone costs
    arr_sorted = sorted(arr)
    
    # Precompute Prefix Sums (1-indexed for convenience)
    p1 = [0] * (n + 1)
    p2 = [0] * (n + 1)

    for i in range(n):
        p1[i+1] = p1[i] + arr[i]
        p2[i+1] = p2[i] + arr_sorted[i]

    # Number of queries
    m = int(input())

    for _ in range(m):
        typo, l, r = map(int, input().split())
        if typo == 1:
            # Range sum on original array
            print(p1[r] - p1[l-1])
        else:
            # Range sum on sorted array
            print(p2[r] - p2[l-1])

if __name__ == "__main__":
    solve()