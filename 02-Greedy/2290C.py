"""
Day 173: Codeforces 2290C - Books on a Shelf
Topic: Greedy / Constructive / Sorting / Observation

Question Extraction:
- Given n books with heights h_i. Arrange them in any order on a shelf.
- A book is visible from the left if it is strictly taller than every book
  to its left, and visible from the right if it is strictly taller than
  every book to its right.
- Find the maximum number of books visible from at least one side, and print
  one arrangement achieving it.

Why we did this (Approach & Intuition):
- Visibility needs strictly taller, so two books of the same height can never
  both be visible from the same side. For one height value, at most one copy
  can be left-visible and at most one copy can be right-visible.
  So each height contributes at most min(count, 2) visible books.
- Upper bound: k <= sum over distinct heights of min(count, 2).
- This bound is achievable. Take one copy of each distinct height and place
  them in increasing order on the left: every one of them is left-visible.
  Take a second copy of each height that has one and place them in decreasing
  order on the right: every one of them is right-visible.
- Any remaining copies (3rd, 4th, ...) go in the middle. They are hidden
  from the left (the tallest left-group book is already >= them) and hidden
  from the right (a copy of the same height sits in the right group, so
  nothing strictly smaller than it can be visible from there). They do not
  hurt any visible book.
- Layout: [distinct ascending] + [extra copies] + [second copies descending].
- Check the maximum height M: if it has 2+ copies, the left group ends with M
  and the right group starts with M, both visible. If it has 1 copy, it is
  the last of the left group and visible from the left.

Logic:
1. Sort h.
2. Walk through the sorted array and count the occurrence number of each value:
     1st occurrence -> l, 2nd occurrence -> r, 3rd or later -> mid.
3. k = len(l) + len(r).
4. Print k, then l + mid + reversed(r).

Complexity:
- Time: O(n log n) per test case (sorting). Space: O(n).

Pitfalls hit while solving:
- Visibility is strict, so equal heights cannot both be visible from one side.
- Cap each height at 2 visible books, not 1.
- Extras go in the middle, and the right group must be reversed to be
  decreasing.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))

        h.sort()
        l, r, mid = [], [], []
        cnt = 0

        for i in range(n):
            if i > 0 and h[i] == h[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 1:
                l.append(h[i])
            elif cnt == 2:
                r.append(h[i])
            else:
                mid.append(h[i])

        k = len(l) + len(r)
        ans = l + mid + r[::-1]

        print(k)
        print(*ans)

if __name__ == "__main__":
    solve()