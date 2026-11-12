"""
Day 173: Codeforces 2290B - Stubborn Pen
Topic: Greedy / Strings / Observation / Implementation

Question Extraction:
- A pen starts in red. After writing a letter, its color flips automatically
  (red -> blue, blue -> red).
- Before writing any letter, you may switch the color manually.
- Write a string s of R and B, where the i-th letter must be written in the
  color s_i.
- Find the minimum number of manual switches needed.

Why we did this (Approach & Intuition):
- Without manual switches, the pen alternates colors. So we only need to
  check, for each letter, whether the pen's natural color already matches.

- First letter: the pen starts red.
    s[0] == 'R' -> no switch needed.
    s[0] == 'B' -> one switch needed.

- Letter i (i >= 1): the previous letter was written in color s[i-1], so the
  pen now naturally holds the OPPOSITE color.
    s[i] != s[i-1] -> the natural color already matches, no switch.
    s[i] == s[i-1] -> the pen holds the wrong color, one switch needed.

- Each decision depends only on the previous letter, because a manual switch
  right before writing still leaves the pen flipping from the written color
  afterwards. The state after writing s[i] is always "opposite of s[i]",
  regardless of whether we switched. So the choices are independent and the
  count is simply the sum of the forced switches.

- Answer = (s[0] == 'B') + number of adjacent equal pairs.

Logic:
1. c = 1 if s[0] == 'B', else 0.
2. For every i from 0 to n-2, if s[i] == s[i+1], c += 1.
3. Print c.

Complexity:
- Time: O(n) per test case. Space: O(n) for the string.

Pitfalls hit while solving:
- The pen starts red, so a leading 'B' costs one switch.
- Equal adjacent letters need a switch, different adjacent letters are free.
- The switches never interact, so greedy counting is exactly optimal.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        c = 0

        if s[0] == 'B':
            c += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                c += 1
        print(c)

if __name__ == "__main__":
    solve()