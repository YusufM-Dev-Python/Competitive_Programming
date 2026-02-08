# Day 9: Line Trip (Codeforces 1901A)
# Folder: Greedy
# Logic: Greedy Gap Calculation. We identify the maximum distance between 
# refueling points. The final stretch to 'x' is doubled for the round trip.
# Time Complexity: O(n) - Single pass through the stations.
# Space Complexity: O(n) - Storing the list of stations.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        # n: number of stations, x: the destination point
        n, x = map(int, input().split())
        s = list(map(int, input().split()))

        # Start: Gap from origin (0) to the first station
        gap_max = s[0]
        
        # Intermediate: Gaps between all consecutive stations
        for i in range(1, n):
            gap = s[i] - s[i-1]
            if gap > gap_max:
                gap_max = gap

        # The Return Constraint: Gap from last station to x and back
        last_gap = 2 * (x - s[-1])
        if last_gap > gap_max:
            gap_max = last_gap
        
        print(gap_max)

if __name__ == "__main__":
    solve()