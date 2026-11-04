"""
Day 166: Codeforces 2283B - Rhythmic String[cite: 10]
Topic: Number Theory / Divisibility / Greedy / Combinatorics
Question Extraction:
- We call a binary string `s` periodic if there exists an integer `k` (1 <= k < m) such that s_i = s_{i+k} for every i, and the smallest such `k` is the period `p`[cite: 10].
- A string is rhythmic if it is periodic and among the first `p` characters, there is exactly one '1'[cite: 10].
- We are given an array `a` of `n` integers and a string `s` initially of 10^18 zeros. For each element a_i, characters at positions that are multiples of a_i become '1'[cite: 10].
- Before performing these changes, we may remove any elements from `a` to find the minimum number of elements that need to be removed so that the resulting string `s` is rhythmic[cite: 10].

Why we did this (Approach & Intuition):
- For the resulting string to be rhythmic with period `p`, the elements we choose to keep in our array must share a common structural relationship (such as multiples of a base value or divisibility properties) that cleanly dictates the minimum removals (`n - ans`).
- By counting how many elements satisfy divisibility relationships (`y % x == 0`) for each candidate element in `a`, we can identify the optimal subset size (`ans`) that maximizes compatibility without triggering conflicts.
- Subtracting this maximum compatible subset size from `n` gives the minimum number of elements required for removal.

Logic:
1. Read the number of test cases `t`[cite: 10].
2. For each test case, read length `n` and array `a`[cite: 10].
3. For each element `x` in `a`, count how many elements `y` in `a` are divisible by `x` (`y % x == 0`).
4. Track the maximum count (`ans`) of such compatible elements.
5. Print `n - ans` as the minimum elements to remove.

Complexity Analysis:
- Time: O(N^2) per test case - nested loops checking divisibility across array elements.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = 0
        for x in a:
            cnt = 0
            for y in a:
                if y % x == 0:
                    cnt += 1
            if cnt > ans:
                ans = cnt

        print(n - ans)

if __name__ == "__main__":
    solve()