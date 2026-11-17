"""
Day 178: Codeforces 2161C - Loyalty
Topic: Greedy / Sorting / Two Pointers / Constructive / Math

Question Extraction:
- You buy n items with prices a_i, where 1 <= a_i <= X (X is the loyalty factor).
- Loyalty level = floor(S / X), where S is the total spent so far.
- If buying an item with price p raises your level, you earn p bonus points.
- Choose the purchase order that maximizes the bonus points, and print the
  maximum together with one such order.

Why we did this (Approach & Intuition):
- Since a_i <= X, one purchase can raise the level by at most 1. A purchase
  raises the level exactly when (S % X) + p >= X, where S % X is the
  "progress inside the current level".

- Level-ups are the only thing that earns points, and the total number of
  level-ups is fixed by the final sum: floor(total / X). So we want those
  level-ups to be caused by the LARGEST items, because the item that crosses
  the boundary is the one that pays its price as bonus.

- Greedy with two pointers on the sorted array:
    * If the largest remaining item crosses a boundary now
      ((S % X) + a[h0] >= X), buy it and earn its price.
    * Otherwise, the largest item cannot cross, so NO remaining item can
      cross (it is the max). Buying anything now earns nothing, so spend the
      SMALLEST item. It earns nothing either way, but it pushes S % X up,
      which makes the next large item more likely to cross.
- Small items are "fillers" that set up the remainder, large items are the
  "crossers" that collect the points.

What I missed (my first idea):
- First logic: levels = total // X, so the answer is the sum of the top
  `levels` items.
- The gap: this counts WHICH items should earn points, but not whether an
  order exists that makes all of them cross a boundary. Order matters.
- Example: X = 10, items 4, 6, 10. Total is 20, so 2 levels, top 2 = 10 + 6 = 16.
  If we buy 10 first (earns 10, S = 10), then 6 on its own cannot cross
  (0 + 6 < 10). Buying 6 right away gives only 10 points.
  The fix is to insert the small item 4 as a filler: 10, then 4 (S = 14,
  remainder 4), then 6 (4 + 6 >= 10, crosses, earns 6). Total 16.
- So when the large items cannot change the level on their own, we buy a small
  item first. That small item is the game changer that lets a large item
  cross later.

Logic:
1. Sort a ascending, keep pointers l0 = 0 (smallest) and h0 = n - 1 (largest).
2. Repeat n times: if (S % X) + a[h0] >= X, take a[h0], add it to ans.
   Else take a[l0].
3. Append the taken item to the order and add it to S.
4. Print ans, then the order.

Complexity:
- Time: O(n log n) per test case (sorting). Space: O(n).

Pitfalls hit while solving:
- Top-k by price is only an upper bound on which items earn points. The
  order has to actually make them cross.
- If the largest cannot cross, nothing can, so buy the smallest as filler.
- Use S % X (progress in the current level), not S // X.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n,x = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()

        s = 0
        order = []
        ans = 0
        l0, h0 = 0,n-1
        for _ in range(n):
            if s % x + a[h0] >= x:
                p = a[h0]
                h0 -= 1
                ans += p
            else:
                p = a[l0]
                l0 += 1
            order.append(p)
            s += p

        print(ans)
        print(*order)
            
if __name__ == "__main__":
    solve()