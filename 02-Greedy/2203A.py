"""
Day 177: Codeforces 2203A - Towers of Boxes
Topic: Math / Greedy / Observation / Ceiling Division

Question Extraction:
- Monocarp has n identical boxes, each with weight m and durability d.
- He stacks them into towers, each with at least one box, and uses all n boxes.
- No box may break: for each box, the total weight of all boxes above it
  must not exceed its durability d.
- Find the minimum number of towers.

Why we did this (Approach & Intuition):
- Inside a tower of height h, the bottom box carries the most weight:
  the h - 1 boxes above it, i.e. (h - 1) * m. Every other box carries less,
  so the bottom box is the only one we need to check.
- The condition (h - 1) * m <= d gives h - 1 <= d // m, so
      max height of one tower H = d // m + 1.
  (In the code this value is stored in `total_piles`. It is really the
  maximum number of boxes per tower, not a count of towers.)
- To minimize the number of towers, make each tower as tall as allowed.
  Every tower holds at most H boxes, so we need at least ceil(n / H) towers,
  and that many is achievable by filling towers of height H and one shorter
  tower with the remainder. A shorter tower is always safe.
- Answer = ceil(n / H) = n // H, plus 1 if n % H != 0.

Logic:
1. H = d // m + 1 (max boxes per tower).
2. curr_ans = n // H.
3. If n % H == 0, print curr_ans, otherwise print curr_ans + 1.

Complexity:
- Time: O(1) per test case. Space: O(1).

Pitfalls hit while solving:
- The +1 in d // m + 1 counts the bottom box itself, since only the boxes
  ABOVE it add weight.
- If m > d, then d // m = 0 and H = 1, so every box is its own tower.
- Round the division up, because leftover boxes still need a tower.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n,m,d = map(int,input().split())


        total_piles = d//m + 1

        curr_ans = n//total_piles
        if n % total_piles == 0:
            print(curr_ans)
        else:
            print(curr_ans + 1)


if __name__ == '__main__':
    solve()