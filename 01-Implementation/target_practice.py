"""
Day 13: Target Practice (Codeforces 1873C)
Problem Link: https://codeforces.com/contest/1873/problem/C

Logic:
The grid is a 10x10 target. Points are awarded based on which 'ring' the 
'X' falls into. We calculate the distance of each 'X' from the 4 edges:
Top (i), Bottom (9-i), Left (j), and Right (9-j). 
The minimum of these distances determines the ring layer (0-indexed), 
so we add 1 to get the actual score (1-5).

Complexity Analysis:
- Time: O(1) per test case (since the grid is always a fixed 10x10).
- Space: O(1) to store the grid and score.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        grid = []
        # Read the 10x10 grid
        for _ in range(10):
            grid.append(input())
        
        total_score = 0

        # Scan every cell in the grid
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 'X':
                    # Find distance to the closest horizontal and vertical edges
                    row_dist = min(i, 9 - i)
                    col_dist = min(j, 9 - j)

                    # The ring level is the minimum of these distances + 1
                    point = min(row_dist, col_dist) + 1
                    total_score += point
                    
        print(total_score)

if __name__ == "__main__":
    solve()