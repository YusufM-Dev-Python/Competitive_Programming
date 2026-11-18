"""
Day 179: Codeforces 2227B - Party Monster
Topic: Strings / Brackets / Observation / Constructive

Question Extraction:
- Given a bracket string s of length n containing only '(' and ')'.
- Operation (at most once): choose a substring, remove it, then reinsert its
  characters one by one at any positions in the remaining string.
- Decide whether the string can become a regular bracket sequence.

Why we did this (Approach & Intuition):
- The operation never changes the multiset of characters, only their order.
  A regular bracket sequence needs the number of '(' to equal the number of
  ')', so equal counts are necessary.
- Equal counts are also sufficient. Choose the substring to be the WHOLE
  string. After removing it, the remaining string is empty, and we can
  reinsert the characters in any order we like. Place all the '(' first
  and then all the ')': "((...))" is regular.
- So the substring/reinsertion detail is a distraction. Taking the whole
  string gives full freedom to rearrange, and the only real constraint is
  the count balance.

Logic:
1. Count o = number of '(' and c = number of ')'.
2. Print YES if o == c, otherwise NO.

Complexity:
- Time: O(n) per test case. Space: O(n) for the string.

Pitfalls hit while solving:
- Do not simulate the removal or reinsertion. Choosing the whole string
  makes any arrangement reachable.
- An odd n always gives NO, which is already covered by o != c.
"""

import sys
from math import gcd, lcm
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        o = 0
        c = 0
        for i in range(n):
            if s[i] == '(':
                o += 1
            else:
                c += 1

        if o == c:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()