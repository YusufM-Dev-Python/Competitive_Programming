"""
Day 40: Points on Line (Codeforces 252C)
Problem Link: https://codeforces.com/contest/252/problem/C

Logic:
1. Since the points are sorted, for each point 'l', find the furthest 
   point 'r' such that arr[r] - arr[l] <= d.
2. The number of points in between (excluding 'l') is m = r - l - 1.
3. If we pick 'l' as our first point, we need to pick 2 more points 
   from the remaining 'm' points. 
4. The number of ways to do this is mC2 = m * (m - 1) / 2.
5. Sum these combinations for all possible 'l'.

Complexity Analysis:
- Time: O(N) - Both 'l' and 'r' pointers traverse the array once.
- Space: O(N) - To store the coordinates.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input().split()
    if not line1: return
    n, d = map(int, line1)

    arr = list(map(int, input().split()))

    r = 0
    score = 0

    # Two Pointers approach
    for l in range(n):
        # Expand the right pointer as long as the distance is <= d
        while r < n and arr[r] - arr[l] <= d:
            r += 1
        
        # 'r' is now at the first index that FAILS the condition.
        # The number of points in the range (arr[l+1]...arr[r-1]) is:
        m = r - l - 1
        
        # If there are at least 2 other points, calculate combinations mC2
        if m >= 2:
            score += m * (m - 1) // 2

    print(score)

if __name__ == "__main__":
    solve()