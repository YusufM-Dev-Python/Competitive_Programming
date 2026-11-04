"""
Day 166: Codeforces 2283A - Numbers on the Board[cite: 9]
Topic: Math / Case Analysis / Implementation
Question Extraction:
- All integers from `l` to `r` inclusive are written on the board, each exactly once[cite: 9].
- A number is called `beautiful` if it is equal to the sum of all numbers currently on the board (including itself)[cite: 9].
- We can erase any numbers from the board (keeping at least one), and we want to find the minimum number of erasures needed so that at least one remaining number becomes beautiful[cite: 9].

Why we did this (Approach & Intuition):
- The sum of an arithmetic sequence from `l` to `r` can be calculated, and we want a remaining number `x` to equal the sum of all remaining numbers.
- By analyzing the ranges of `l` and `r` (positive ranges, negative ranges, or ranges spanning across zero), we can evaluate how many elements need to be stripped away.
- When `l > 0` or `r < 0`, all numbers share the same sign, meaning erasures scale with the span size `abs(r - l)`. When the range spans across zero (`l <= 0` and `r >= 0`), the negative and positive values balance out differently, leading to the condition `max(0, abs(r + l) - 1)`.

Logic:
1. Read the number of test cases `t`[cite: 9].
2. For each test case, read `l` and `r`[cite: 9].
3. Check the sign partitions:
   - If `l > 0` or `r < 0`, set `ans = abs(r - l)`.
   - Otherwise, set `ans = max(0, abs(r + l) - 1)`.
4. Print the minimum number of erasures required for each test case.

Complexity Analysis:
- Time: O(1) per test case - constant time arithmetic checks.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        ans = 0
        if (l > 0) or (r < 0): 
            ans = abs(r - l)
        else: 
            ans = max(0, abs(r + l) - 1)

        print(ans)

if __name__ == "__main__":
    solve()