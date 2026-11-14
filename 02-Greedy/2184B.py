"""
Day 175: Codeforces 2184B - Hourglass
Topic: Math / Observation / Simulation / Casework

Question Extraction:
- An hourglass measures s minutes. It is flipped at time 0 and then every k
  minutes (flips happen even if sand is still falling).
- Vadim leaves at minute m and stops flipping (a flip exactly at minute m
  still happens).
- Find how many more minutes the sand keeps falling after he leaves.

Why we did this (Approach & Intuition):
- Let f = m // k be the number of flips after the initial one, and
  rem = m % k the time elapsed since the last flip (or since the start if
  f = 0). The answer is max(0, top - rem), where top is the amount of sand
  in the top half at the moment of the last flip.

- Case s <= k:
  The sand always finishes before the next flip. Each flip restarts a full
  hourglass, so at the last flip top = s.
  Answer = max(0, s - rem).
  If rem = 0 (flip exactly at m), the answer is s.

- Case s > k:
  The sand never finishes between flips, so track top / bottom.
  Start: top = s, bottom = 0.
  After the first k minutes: top = s - k, bottom = k. Flip -> top = k.
  The next k minutes drain exactly k from the top: top = 0, bottom = s.
  Flip -> top = s, bottom = 0. Back to the start state.
  So the state at each flip alternates with period 2:
      f even -> top = s
      f odd  -> top = k
  Since top >= k > rem, the sand is still falling at minute m, and
  the answer is top - rem. (max(0, ...) keeps it safe.)

- Both cases use the same formula, only the value of top differs.

Logic:
1. rem = m % k, flips = m // k.
2. If s <= k: ans = max(0, s - rem).
3. Else: top = s if flips is even, else k. ans = max(0, top - rem).
4. Print ans.

Complexity:
- Time: O(1) per test case. Space: O(1).

Pitfalls hit while solving:
- Flips happen even while sand is still falling, which is what makes s > k
  tricky. Think in terms of top / bottom amounts, not just time.
- The state of the hourglass repeats every 2 flips when s > k.
- A flip exactly at minute m counts: rem = 0 leaves the full top amount.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        s, k, m = map(int, input().split())

        rem = m % k
        flips = m // k

        if s <= k:
            ans = max(0, s - rem)
        else:
            top = s if flips % 2 == 0 else k
            ans = max(0, top - rem)

        print(ans)

if __name__ == "__main__":
    solve()