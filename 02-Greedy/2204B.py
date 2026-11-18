"""
Day 179: Codeforces XXXX - Right Maximum
Topic: Arrays / Observation / Prefix Maximum / Simulation

Question Extraction:
- Given an array a of n integers.
- While the array is non-empty, one operation does two things:
    1. pick the maximum element (the RIGHTMOST one if there are ties),
    2. delete that element and everything after it.
- Count the number of operations until the array is empty.

Why we did this (Approach & Intuition):
- Each operation cuts the array down to a prefix, so the whole process is
  just repeated prefix cutting. The question is which elements get picked.
- Claim: an element gets picked exactly when it is >= every element before
  it, i.e. it is a non-strict prefix maximum.
    * If some earlier element is strictly larger, then whenever our element
      is still in the array, that larger element is too (it sits to the left),
      so ours can never be the maximum. It only disappears when something
      to its left is picked.
    * If every earlier element is <= it, then once everything to its right
      is cut away, it is the rightmost maximum of the remaining prefix, so
      it will be picked.
- Ties matter: an equal earlier element does not block us, because the
  rightmost maximum is chosen, and the equal element to the left gets its
  own turn later. So the comparison is anchor <= a[i+1], not strictly less.
- Check on [1, 3, 2, 3, 1]: operations pick the 3 at index 3, then the 3 at
  index 1, then the 1 at index 0. That is 3 operations, and the non-strict
  prefix maxima are 1, 3, 3, which is also 3.

Logic:
1. anchor = a[0] and ans = 1, because the first element is always counted.
2. Scan left to right. If a[i+1] >= anchor, set anchor = a[i+1] and ans += 1.
3. Print ans.

Complexity:
- Time: O(n) per test case. Space: O(n) for the array.

Pitfalls hit while solving:
- Use >= (not >): equal values each get their own operation.
- The first element is always an operation, so ans starts at 1.
- No need to simulate the deletions, which would be O(n^2) in the worst case.
"""

import sys
from math import gcd, lcm
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        anchor = a[0]
        ans = 1

        for i in range(n-1):
            if anchor <= a[i+1] and i+1 != n:
                anchor = a[i+1]
                ans += 1
        print(ans)

if __name__ == "__main__":
    solve()