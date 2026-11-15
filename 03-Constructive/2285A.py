"""
Day 176: Codeforces 2285A - Composite Permutation
Topic: Math / Constructive / Number Theory / Observation

Question Extraction:
- Given n, build a permutation p of 1..n such that i * p_i is composite
  for every i from 1 to n.
- If no such permutation exists, print -1.

Why we did this (Approach & Intuition):
- For i = 1, the product is 1 * p_1 = p_1, so p_1 itself must be composite.
  The smallest composite is 4, so we need n >= 4.
- Small n:
    n = 1 -> p = [1], product 1 is not composite -> -1
    n = 2 -> p_1 would have to be composite, but only 1, 2 exist -> -1
    n = 3 -> same issue, 1, 2, 3 are not composite -> -1
  So n <= 3 means -1.
- For n >= 4, use the permutation
      [4, 3, 2, 1, 5, 6, 7, ..., n]
  Check each position:
    i = 1: 1 * 4 = 4  (composite)
    i = 2: 2 * 3 = 6  (composite)
    i = 3: 3 * 2 = 6  (composite)
    i = 4: 4 * 1 = 4  (composite)
    i >= 5: i * i is a perfect square of an integer >= 2, so it has the
            divisor i (with 1 < i < i*i), hence composite.
- The block [4, 3, 2, 1] fixes the first four positions, and the identity
  handles the rest because every square of i >= 2 is composite.

Logic:
1. If n <= 3, print -1.
2. Otherwise print [4, 3, 2, 1] followed by 5, 6, ..., n.

Complexity:
- Time: O(n) per test case. Space: O(n).

Pitfalls hit while solving:
- Position 1 forces p_1 to be composite, which is the key observation.
- The identity cannot be used for positions 1 to 4: 1 is not composite and
  2*2, 3*3 are fine, but 1*1 = 1 breaks it, so the first four are rearranged.
- Squares of i >= 2 are always composite, so the tail stays untouched.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        if n <= 3:
            print(-1)
            continue

        ans = [4, 3, 2, 1] + list(range(5, n + 1))
        print(*ans)

if __name__ == "__main__":
    solve()