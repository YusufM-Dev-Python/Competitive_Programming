"""
Day 18: Stripes (Codeforces 1742C)
Problem Link: https://codeforces.com/contest/1742/problem/C

Logic:
A grid is painted with horizontal Red stripes and vertical Blue stripes. 
The stripes are drawn one by one, covering previous colors.
- If a horizontal row is entirely 'R', it means Red was the last to be 
  painted in that area (if it weren't, Blue vertical lines would cross it).
- If no such Red row exists, then Blue must have been the last stripe painted.

Complexity Analysis:
- Time: O(1) - The grid size is fixed at 8x8 (64 cells per test case).
- Space: O(1) - We only store the current row and the result.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        # Consume the blank line provided between test cases
        input()
        
        ans = "B"
        # Scan the 8x8 grid
        for _ in range(8):
            row = input()
            # If we find a solid Red horizontal line, Red was last
            if row == "RRRRRRRR":
                ans = "R"
        
        print(ans)

if __name__ == "__main__":
    solve()