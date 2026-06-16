"""
Day 80 (Bonus): Password (Codeforces 1743A)
Topic: Math / Combinatorics
Logic:
1. We need to find the number of valid 4-digit passwords that can be created using 
   exactly 2 distinct digits, each appearing twice.
2. The input gives 'n' digits that cannot be used, leaving (10 - n) available digits.
3. First, we choose 2 digits out of the remaining (10 - n) digits:
   Ways = (10 - n) * (10 - n - 1) // 2
4. Next, for any 2 selected digits (e.g., X and Y), the number of ways to arrange 
   them into a 4-digit password (XXYY, XYXY, etc.) is 4! / (2! * 2!) = 6.
5. Total configurations = (Ways) * 6.

Complexity Analysis:
- Time: O(1) per testcase - Direct mathematical calculation.
- Space: O(1) - Beyond storing the input array.
"""

import sys

input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        # Combinatorics: C(10-n, 2) * 6
        print(((10 - n) * (10 - n - 1) // 2) * 6)

if __name__ == "__main__":
    solve()