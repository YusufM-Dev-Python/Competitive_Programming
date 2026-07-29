"""
Day 114: 702C - Cellular Network
Topic: Two Pointers / Greedy
Goal: Find the minimum cellular network radius 'r' such that every city 
      has at least one tower within distance 'r'.

Logic:
1. Two Pointers Strategy: We are given sorted coordinates for cities (`n_a`) and towers (`m_a`). 
   For each city, we want to find the nearest tower.
2. Pointer Advancement: We maintain a pointer `r` for the towers. As we iterate through each city 
   using `l`, we greedily move the tower pointer `r` forward as long as the next tower is closer 
   to the current city than (or equally close as) the current tower.
3. Distance Evaluation: Once we find the closest tower for a city, we record that minimum distance. 
   The overall answer (`curr_max`) will be the maximum of these minimum distances across all cities.

Complexity Analysis:
- Time: O(N + M) - Each city and tower pointer moves forward linearly without backtracking.
- Space: O(N + M) to store the coordinate arrays.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, m = map(int, input().split())
    n_a = list(map(int, input().split()))
    m_a = list(map(int, input().split()))

    curr_max = 0
    r = 0

    # Iterate through each city using pointer l
    for l in range(n):
        # Move the tower pointer right as long as the next tower is closer or equidistant
        while r + 1 < m and abs(n_a[l] - m_a[r]) >= abs(n_a[l] - m_a[r + 1]):
            r += 1
        
        # Track the maximum distance required among all closest tower-city pairs
        curr_max = max(curr_max, abs(n_a[l] - m_a[r]))

    print(curr_max)

if __name__ == "__main__":
    solve()