"""
Day 74: Fancy Fence (Codeforces 270A)
Topic: Geometry / Math
Logic:
1. In a regular n-sided polygon, each interior angle 'a' is given by:
   a = (n - 2) * 180 / n
2. Rearranging this to solve for n:
   n * a = 180n - 360
   360 = n * (180 - a)
   n = 360 / (180 - a)
3. For a regular polygon to exist, n must be an integer (and n >= 3).
4. Therefore, the exterior angle (180 - a) must perfectly divide 360.

Complexity Analysis:
- Time: O(1) per test case.
- Space: O(1).
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        a = int(input())

        # (180 - a) is the exterior angle. 
        # 360 divided by the exterior angle gives the number of sides.
        if 360 % (180 - a) == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()