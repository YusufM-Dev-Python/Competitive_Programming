"""
Day 176: Codeforces 2285C - Max Substitution
Topic: Math / Combinatorics / Sorting / Counting / Observation

Question Extraction:
- Given an array a of length n.
- One operation: if the largest element is UNIQUE, replace it with any
  integer x with 1 <= x < max(a). The operation is allowed only when a has
  a unique largest element.
- Count the distinct arrays obtainable with any number of operations
  (including zero), modulo 1e9 + 7.

Why we did this (Approach & Intuition):
- Sort values in descending order: a_0 >= a_1 >= ... >= a_{n-1}.
  If a_0 == a_1, the maximum is not unique, no operation is possible, and
  the answer is 1.

- Otherwise, think about which elements have been "touched" (replaced at
  least once). The operation always acts on the current maximum, so the
  touched elements are always a prefix of the sorted order:
  a_0, a_1, ..., a_i for some i.

- Fix i as the last touched element. When a_i is operated on, it is the
  unique maximum. So:
    * every element touched earlier is currently < a_i,
    * every untouched element is a_{i+1}, ... and must be < a_i.
  The last operation turns a_i into something < a_i.
  So in the final array, positions 0..i hold values in [1, a_i - 1] and
  positions i+1..n-1 keep their original values.

- Every choice of values in [1, a_i - 1] for these i+1 positions is reachable.
  Process a_0 first and set it directly to its final value. That value is
  < a_i <= a_1, so a_1 becomes the unique maximum. Then a_1, then a_2, and
  so on, up to a_i. Each of them is the unique maximum when its turn comes.
  This gives (a_i - 1)^(i+1) arrays for group i.

- Groups never overlap. In group i, position i+1 still holds its original
  value, while in group i+1 it was changed to something smaller. Together
  with the original array (the "zero operations" case), the groups give the
  full count.

- Group i is only valid if a_i is strictly greater than a_{i+1}; otherwise
  a_i is not unique when it needs to be operated on. The first equality
  stops everything after it.

- Answer = 1 + sum over valid i of (a_i - 1)^(i + 1), taken mod 1e9 + 7.

Logic:
1. Sort a in descending order and set ans = 1 for the original array.
2. For i = 0, 1, ...: if a[i] == a[i+1], stop. Otherwise add
   pow(a[i] - 1, i + 1, MOD).
3. Print ans mod 1e9 + 7.

Complexity:
- Time: O(n log n) for the sort, and the modular powers add O(n log n).
- Space: O(n).

Pitfalls hit while solving:
- Ties at the top block everything: if a_i == a_{i+1}, group i and all later
  groups are impossible, so break.
- Values with a_i = 1 contribute 0^(i+1) = 0, which is correct because no
  smaller positive integer exists.
- Use modular pow, since the exponent and base are both large.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort(reverse=True)
        ans = 1
        for i in range(n):
            if i + 1 < n and a[i] == a[i + 1]:
                break
            ans += pow(a[i] - 1, i + 1, MOD)

        print(ans % MOD)

if __name__ == "__main__":
    solve()