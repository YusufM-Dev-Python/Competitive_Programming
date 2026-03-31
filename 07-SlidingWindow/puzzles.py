"""
Day 45: Puzzles (Codeforces 337A)
Problem Link: https://codeforces.com/contest/337/problem/A

Logic:
1. We need to choose 'n' puzzles out of 'm' such that the difference 
   between the largest and smallest complexity is minimized.
2. Sort the list of complexities.
3. Use a sliding window of size 'n' to find the minimum difference
   between the first and last element of the window.

Complexity Analysis:
- Time: O(M log M) - Due to sorting the m puzzles.
- Space: O(M) - To store the puzzle complexities.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: students, m: puzzles
    line1 = input().split()
    if not line1: return
    n, m = map(int, line1)
    
    f = list(map(int, input().split()))

    # Sorting ensures the 'closest' puzzles are neighbors
    f.sort()
    
    min_diff = float('inf')
    
    # Slide a window of size 'n' across the sorted array
    for i in range(m - n + 1):
        # Current difference: (largest in window) - (smallest in window)
        diff = f[i + n - 1] - f[i]
        min_diff = min(min_diff, diff)
        
    print(min_diff)
        
if __name__ == "__main__":
    solve()