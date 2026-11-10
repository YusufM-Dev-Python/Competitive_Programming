"""
Day 171: Codeforces 2179C - Blackslex and Number Theory
Topic: Math / Number Theory / Observation / Sorting

Question Extraction:
- Given an array a of n distinct positive integers.
- One operation: pick an index i and an integer x >= k, then set a_i := a_i mod x.
- Find the maximum k such that some sequence of operations makes all
  elements equal.

Why we did this (Approach & Intuition):
- A mod never increases a value, and if x > a_i it changes nothing.
  Sort a so that a1 < a2 < ... < an. The final common value is at most a1.

- Case k <= a1 (always achievable):
  Pick x = a_i for every element. Then a_i mod a_i = 0, and x = a_i >= a1 >= k
  is legal. Everything becomes 0, so k = a1 always works.

- Case k > a1:
  a1 can never change, since any legal x >= k > a1 gives a1 mod x = a1.
  So the final value must be a1, and every other element must be reduced to a1.
  To get a_i mod x = a1 we need x > a1 and x | (a_i - a1), so x <= a_i - a1.
  The tightest element is a2: x <= a2 - a1, hence k <= a2 - a1.
  Chaining several mods only makes it stricter (it needs a2 - a1 >= 2k).

- Is k = d = a2 - a1 actually achievable when d > a1?
  Use x = a_i - a1 for each i. This x is >= d = k, and x > a1 because
  x >= d > a1. Then a_i mod (a_i - a1) = a1, so all elements become a1.

- Answer = max(a1, a2 - a1).
  If d > a1 we can beat a1 by using k = d, otherwise k = a1 is the best.

Logic:
1. Sort the array.
2. d = b[1] - b[0] (gap between the two smallest elements).
3. Print d if d > b[0], else b[0].

Complexity:
- Time: O(n log n) per test (sorting). Only the two smallest elements matter,
  so a linear scan for the two minima gives O(n).
- Space: O(n).

Pitfalls hit while solving:
- Only the two smallest elements matter. The rest follow automatically.
- k = a1 is always safe (everything becomes 0), so the answer is never below a1.
- Distinct values guarantee d > 0.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        b.sort()
        d = b[1] - b[0]
        print(d if d > b[0] else b[0])

if __name__ == "__main__":
    solve()