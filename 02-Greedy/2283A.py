"""
Day 168: Codeforces 2284A - A1. 15K4JR3B (Easy Version)
Topic: Math / Greedy / Geometry Optimization
Question Extraction:
- Three points A, B, and C start at the origin (0, 0)[cite: 12].
- We perform exactly `n` operations, where in each operation we choose one point and increase or decrease one of its coordinates by 1[cite: 12].
- We need to find the maximum doubled area of triangle ABC after all operations are completed[cite: 12].

Why we did this (Approach & Intuition):
- To maximize the doubled area of the triangle formed by three points given `n` total coordinate increments, we want to distribute the operations to form orthogonal or maximally spread components (like a base and a height).
- By splitting `n` into two balanced parts (base and height), we maximize their product. If `n` is even, we split it evenly into `n // 2` and `n // 2`. If `n` is odd, one dimension gets `n // 2` and the other gets `n // 2 + 1`.
- Multiplying these optimal components gives the maximum possible doubled area.

Logic:
1. Read the number of test cases `t`[cite: 12].
2. For each test case, read the integer `n`[cite: 12].
3. Determine `base` and `height`:
   - If `n` is even, `base = n // 2` and `height = n // 2`.
   - If `n` is odd, `base = n // 2` and `height = n // 2 + 1`.
4. Print the product `base * height` as the maximum doubled area.

Complexity Analysis:
- Time: O(1) per test case - constant time arithmetic calculation.
- Space: O(1) - constant memory.
"""

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        base = 0
        height = 0
        if n % 2 == 0:
            base = n // 2
            height = n // 2
        else:
            base = n // 2
            height = n // 2 + 1

        print(base * height)

if __name__ == "__main__":
    solve()