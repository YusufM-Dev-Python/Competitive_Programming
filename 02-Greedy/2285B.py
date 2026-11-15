"""
Day 176: Codeforces 2285B - Diverse String
Topic: Math / Counting / Greedy / Observation / Binary String

Question Extraction:
- The diversity of a binary string s is the number of distinct strings
  obtainable by doing at most one operation: choose x in {0, 1} and a
  segment [l, r], then set every character in it to x.
- Before that, we may toggle at most k characters of s.
- Maximize the diversity of the resulting string.

Why we did this (Approach & Intuition):
- Let z = number of zeros and o = number of ones, with z + o = n.
  Count the distinct strings obtainable from a fixed s:

  1. No operation: the original string, 1 string.

  2. x = 0 on [l, r]: the segment turns into zeros, so only the ones inside
     it matter. The result depends only on which consecutive block of ones
     (the i-th through j-th one) lies inside the segment. Every non-empty
     block gives a different string, so there are o(o+1)/2 strings.
     Segments with no ones give back s itself, already counted.

  3. x = 1 on [l, r]: by symmetry, z(z+1)/2 strings.

  4. These groups never overlap:
     - the x = 0 results have fewer ones than s,
     - the x = 1 results have more ones than s,
     - the original has exactly o ones.

  Diversity = 1 + z(z+1)/2 + o(o+1)/2.
  Check: "10" -> 1 + 1 + 1 = 3, matching the statement.

- Maximize over toggles. With z + o = n, the quantity z^2 + o^2 is convex,
  so it grows as the split becomes more unbalanced.
  Toggling a majority character only reduces the imbalance, so every toggle
  should go from the minority to the majority.
- Toggle min(z, o) characters at most k times, so the minority count becomes
  max(0, minority - k) and the other count becomes n minus that.

Logic:
1. z = count of '0', o = n - z.
2. If z <= o: zz = max(0, z - k), oo = n - zz.
   Else:      oo = max(0, o - k), zz = n - oo.
3. Print 1 + zz(zz+1)//2 + oo(oo+1)//2.

Complexity:
- Time: O(n) per test case (counting). Space: O(n) for the string.

Pitfalls hit while solving:
- Do not forget the +1 for the original string (the "at most once" case).
- Equal results across x = 0 and x = 1 are impossible, so just add the counts.
- Toggle only the minority, and clamp at 0 so k > minority does not go negative.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()

        z = s.count('0')
        o = n - z
        if z <= o:
            zz = max(0, z - k)
            oo = n - zz
        else:
            oo = max(0, o - k)
            zz = n - oo
        print(1 + zz * (zz + 1) // 2 + oo * (oo + 1) // 2)

if __name__ == "__main__":
    solve()