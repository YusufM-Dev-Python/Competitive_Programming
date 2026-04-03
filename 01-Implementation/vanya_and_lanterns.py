"""
Day 46: Vanya and Lanterns (Codeforces 492B)
Problem Link: https://codeforces.com/contest/492/problem/B

Logic:
1. Sort the lantern positions to calculate gaps between them.
2. The distance between two adjacent lanterns needs a radius of at least (gap / 2).
3. The distance from 0 to the first lantern needs a radius of at least (arr[0] - 0).
4. The distance from the last lantern to the end 'l' needs a radius of (l - arr[n-1]).
5. The answer is the maximum of these three values.

Complexity Analysis:
- Time: O(N log N) - Due to sorting the lantern positions.
- Space: O(N) - To store the lantern coordinates.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line1 = input().split()
    if not line1: return
    n, l = map(int, line1)
    
    arr = list(map(int, input().split()))
    arr.sort()

    # Find the maximum gap between any two internal lanterns
    max_gap = 0
    for i in range(n - 1):
        dist = arr[i+1] - arr[i]
        if dist > max_gap:
            max_gap = dist
    
    # Check the three critical constraints
    start_dist = float(arr[0])          # Distance from 0 to first lantern
    end_dist = float(l - arr[n-1])      # Distance from last lantern to l
    mid_dist = max_gap / 2.0            # Half of the largest internal gap

    # The required radius is the maximum of all constraints
    ans = max(start_dist, end_dist, mid_dist)
    
    # Print with high decimal precision
    print(f"{ans:.10f}")

if __name__ == "__main__":
    solve()