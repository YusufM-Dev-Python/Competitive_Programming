"""
Day 147: Codeforces 1615B - Diverse Substring / Bitwise / Prefix Sums
Topic: Bit Manipulation / Prefix Sums / Precomputation
Logic:
1. Precompute prefix sums of set bits for every bit position (from 0 to 18) up to `max_n = 200005`. 
   `ans[i][b]` stores the total number of set bits at position `b` from numbers $1$ to $i$.
2. For each test case, read range `l` and `r`.
3. The total elements in the range are `total_elem = r - l + 1`.
4. For each bit position, find how many numbers have that bit set in the range $[l, r]$ using prefix sums: `ones = ans[r][b] - ans[l-1][b]`.
5. The deletions needed to make all elements share a 1 at bit position `b` is `total_elem - ones`.
6. Take the minimum deletions across all bit positions and print it.

Complexity Analysis:
- Time: O(MAX_N * MIN_B) for precomputation, and O(MIN_B) per testcase for queries.
- Space: O(MAX_N * MIN_B) - to store the prefix sum table.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

max_n = 200005
min_b = 19

ans = [[0]*min_b for i in range(max_n)]

for i in range(1, max_n):
    for b in range(min_b):
        set_bit = (i >> b) & 1
        ans[i][b] = ans[i-1][b] + set_bit

def solve():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())

        total_elem = r - l + 1
        min_del = total_elem

        for b in range(min_b):
            ones = ans[r][b] - ans[l-1][b]
            deletions = total_elem - ones
            min_del = min(deletions, min_del)

        print(min_del)

if __name__ == "__main__":
    solve()