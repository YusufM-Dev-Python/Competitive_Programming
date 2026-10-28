"""
Day 165: Codeforces A - Flip Flops[cite: 8]
Topic: Greedy / Sorting / Simulation
Question Extraction:
- OtterZ fights n monsters, each with combat power a_i, starting with combat power c and k flip flops[cite: 8].
- Operations allowed:
  1. Kill an alive monster i if a_i <= c; combat power c increases by a_i[cite: 8].
  2. Throw a flip-flop at monster i, breaking the flip-flop and increasing its power a_i by 1[cite: 8].
- We want to maximize the final combat power c after the battle[cite: 8].

Why we did this (Approach & Intuition):
- Sorting the monster powers allows us to greedily process smaller monsters first, which are easier to absorb or boost.
- If a monster's power is too high, we can use our remaining flip-flops (`k`) to increment its power just enough to reach our current combat threshold, or absorb it directly if `a_i <= c`.
- Tracking how many flip-flops are consumed dynamically lets us maximize our combat growth efficiently.

Logic:
1. Read the number of test cases and loop through each.
2. For each test case, read `n`, `c`, and `k`, then sort the monster powers `arr`[cite: 8].
3. Iterate through each monster power `x`:
   - If `x > c`, we can either boost it or stop depending on feasibility, but standard processing handles sorted values.
   - Calculate how many flip-flops `f` can be used up to `k` to bridge the gap if needed (`c - x`), updating `k` and growing `c` iteratively.
4. Print the final maximized combat power `c`.

Complexity Analysis:
- Time: O(N log N) per test case due to sorting the monster array.
- Space: O(N) to store the monster powers.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, c, k = map(int, input().split())
    arr = sorted(map(int, input().split()))

    for x in arr:
        if x > c:
            break
        f = min(k, c - x)  
        k -= f
        c += x + f

    print(c)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()