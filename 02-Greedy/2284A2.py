"""
Day 168: Codeforces 2284A2 - A2. 15K4JR3B (Hard Version)
Topic: Greedy / Sorting / Bitwise Powers / Geometry
Question Extraction:
- Three points A, B, and C start at the origin (0, 0) and we are given an array `a` of length `n`[cite: 13].
- During the i-th operation, we choose one of the points and increase or decrease one of its coordinates by 2 to the power of a_i[cite: 13].
- We need to find the maximum doubled area of triangle ABC after all n operations are performed[cite: 13].

Why we did this (Approach & Intuition):
- To maximize the doubled area of the triangle, we want to split our available power contributions (2^{a_i}) into two balanced components representing our base and height.
- Sorting the array `a` in descending order ensures that we process the largest powers of two first, greedily adding each large power to the smaller of our two tracking dimensions (`base` or `height`) to keep them as balanced as possible.
- Multiplying the finalized `base` and `height` gives the maximum possible doubled area.

Logic:
1. Read the number of test cases `t`[cite: 13].
2. For each test case, read `n` and the array `a` of powers[cite: 13].
3. Sort `a` in descending order to handle the largest powers of two first.
4. Iterate through each element `x` in `a`, compute `ans = 2**x`, and add it to `base` or `height` depending on which is currently smaller or equal, keeping the distribution balanced.
5. Print the product `base * height` as the final maximum doubled area.

Complexity Analysis:
- Time: O(N log N) per test case due to sorting the array of length `n`.
- Space: O(N) to store the input array of powers.
"""

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        base = 0
        height = 0

        a.sort(reverse=True)
        for x in a:
            ans = 2**x
            if base <= height:
                base += ans
            else:
                height += ans
        
        print(base * height)

if __name__ == "__main__":
    solve()