"""
Day 174: Codeforces 2210C1 - A Simple GCD Problem (Easy Version)
Topic: Math / Number Theory / GCD / LCM / Observation

Question Extraction:
- Given arrays a and b of length n, with b_i = a_i in this easy version.
- For each index i you may do at most one operation: pick m != a_i with
  1 <= m <= b_i and set a_i := m.
- After all operations, the gcd of every subarray of length >= 2 must be
  unchanged.
- Find the maximum number of operations that can be performed.

Why we did this (Approach & Intuition):
- Since b_i = a_i, any new value is smaller than a_i, so an operation can only
  shrink a_i. Count the indices that can be shrunk.

- Necessary condition:
  Let g[j] = gcd(a_j, a_{j+1}). The pair gcds must stay the same, so the new
  value of a_i must be a multiple of both neighbouring pair gcds:
      new a_i is a multiple of x_i = lcm(g[i-1], g[i])
  (at the ends: x_0 = g[0], x_{n-1} = g[n-2]).
  The original a_i is also a multiple of both gcds, so x_i divides a_i.

- Sufficiency (why x_i itself is a valid new value):
  Since x_i | a_i, gcd(a_{i-1}, x_i) divides gcd(a_{i-1}, a_i) = g[i-1].
  Since g[i-1] | x_i, g[i-1] divides gcd(a_{i-1}, x_i). So they are equal.
  The same holds for g[i], and for longer subarrays by the same
  divisibility argument. If neighbours are also shrunk to their own x
  values, gcd(x_i, x_{i+1}) = lcm(g[i], gcd(g[i-1], g[i+1])) = g[i], because
  gcd(g[i-1], g[i+1]) divides g[i]. So all indices can be shrunk
  independently.

- Therefore index i can be operated on exactly when x_i < a_i, that is
  x_i != a_i (x_i always divides a_i). Otherwise a_i is already the smallest
  value consistent with its neighbours and nothing smaller works.

- Answer = number of i with x_i != a_i.

Logic:
1. Compute g[j] = gcd(a[j], a[j+1]) for j in 0..n-2.
2. For each i, x = g[0] if i == 0, g[n-2] if i == n-1, else lcm(g[i-1], g[i]).
3. If x != a[i], ans += 1.
4. Print ans.

Complexity:
- Time: O(n log A) per test case (gcd/lcm computations). Space: O(n).

Pitfalls hit while solving:
- End elements depend on only one neighbouring gcd.
- b is identical to a here, so it is read but never used.
- The answer counts indices that can change, not the number of distinct values.
"""

import sys
from math import gcd, lcm
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = input()  # b_i = a_i in the easy version, not needed

        g = [gcd(a[i], a[i + 1]) for i in range(n - 1)]

        ans = 0
        for i in range(n):
            if i == 0:
                x = g[0]
            elif i == n - 1:
                x = g[n - 2]
            else:
                x = lcm(g[i - 1], g[i])
            if x != a[i]:
                ans += 1

        print(ans)

if __name__ == "__main__":
    solve()