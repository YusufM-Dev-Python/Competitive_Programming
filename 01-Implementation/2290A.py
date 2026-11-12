"""
Day 173: Codeforces 2290A - Three Piles
Topic: Math / Observation / Implementation

Question Extraction:
- Three piles with a, b, c stones, given in sorted order (a <= b <= c).
- You must make exactly one move: take one stone from a pile and put it on
  another pile.
- Decide whether, after that single move, all three piles are equal.

Why we did this (Approach & Intuition):
- A move never changes the total, so the final state must be m, m, m with
  total = 3m. If the total is not divisible by 3, the answer is NO.
- Work backwards from (m, m, m). One move changes exactly two piles: the
  source loses 1 and the destination gains 1. So before the move, the piles
  were some arrangement of (m - 1, m, m + 1), where the pile at m + 1 gave
  one stone to the pile at m - 1.
- Since the input is sorted, the only valid starting state is
      a = m - 1, b = m, c = m + 1.
- If a = b = c = m already, the answer is NO. The move is mandatory, so it
  would break the equality (this is the trap in the statement).
- Any other arrangement cannot be fixed by moving one stone.

Logic:
1. total = a + b + c. If total % 3 != 0, print NO.
2. m = total // 3.
3. Print YES iff (a, b, c) == (m - 1, m, m + 1), else NO.

Complexity:
- Time: O(1) per test case. Space: O(1).

Pitfalls hit while solving:
- Already-equal piles give NO, since the single move is forced.
- Divisibility by 3 is necessary but not sufficient, so check the exact
  shape (m - 1, m, m + 1) too.
- The input is guaranteed sorted, so only one ordering needs checking.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())

        total = a + b + c
        if total % 3 != 0:
            print("NO")
            continue

        m = total // 3
        if a == m - 1 and b == m and c == m + 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()