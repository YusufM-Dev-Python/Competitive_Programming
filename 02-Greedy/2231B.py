"""
Day 172: Codeforces 2231B - Another Sorting Problem
Topic: Greedy / Observation / Constructive / Array Segments

Question Extraction:
- Given an array a of n integers.
- You may perform one operation at most once: choose a positive integer k and
  a subsequence of indices, then add k to every element at those indices.
- Decide whether the array can be made nondecreasing.

Why we did this (Approach & Intuition):
- Every element gets either +0 or +k, with one shared k. Mark each index with
  x_i = 1 (chosen) or x_i = 0 (not chosen). Then check each adjacent pair
  (i, i+1) on its own.

- Descent (a[i] > a[i+1]), let d = a[i] - a[i+1]:
  The only way to fix it is x_i = 0 and x_{i+1} = 1, and then we need k >= d.
  So the lower bound is k >= max(d) over all descents = l0.

- Between two consecutive descents there is a nondecreasing run.
  It starts right after a descent, so its first element has x = 1.
  It ends right before the next descent, so its last element has x = 0.
  So x must flip from 1 to 0 somewhere inside the run.
  Flipping 1 -> 0 on an adjacent pair (j, j+1) needs
      a[j] + k <= a[j+1], i.e. k <= a[j+1] - a[j].
  We choose the flip at the biggest step of the run, which gives an upper
  bound k <= max step of that run.
  Taking the minimum over all closed runs gives h0.

- Runs that need no constraint:
  The run before the first descent can use x = 0 everywhere.
  The run after the last descent can use x = 1 everywhere.
  Only runs trapped between two descents add an upper bound.

- A trapped run of length 1 has no step to flip on, so its max step is 0,
  h0 = 0 < l0, and the answer is NO. The code handles this automatically
  because curr_max starts at 0.

- Answer is YES iff some k exists with l0 <= k <= h0, i.e. h0 >= l0.
  With no descents l0 = 0 and h0 = inf, so the answer is YES.

Logic:
1. Scan adjacent pairs once.
2. On a descent: update l0 with the drop. If a run was open, close it by
   h0 = min(h0, curr_max). Then open a new run with curr_max = 0.
3. On a non-descent: if a run is open, curr_max = max(curr_max, step).
4. The final run is never closed, since nothing forces it back to 0.
5. Print YES if h0 >= l0, else NO.

Complexity:
- Time: O(n) per test case. Space: O(n) for the array.

Pitfalls hit while solving:
- Only runs between two descents are constrained. Do not close the last one.
- Take the max step inside a run (best place to flip), then the min over runs.
- Equal neighbours count as steps of size 0, not as descents.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        l0 = 0
        h0 = float('inf')
        seg_open = False
        curr_max = 0

        for i in range(n - 1):
            if a[i] > a[i + 1]:
                l0 = max(l0, a[i] - a[i + 1])
                if seg_open:
                    h0 = min(h0, curr_max)
                seg_open = True
                curr_max = 0
            else:
                if seg_open:
                    curr_max = max(curr_max, a[i + 1] - a[i])

        print("YES" if h0 >= l0 else "NO")

if __name__ == "__main__":
    solve()