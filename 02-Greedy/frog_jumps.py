"""
Day 62: Frog Jumps (Codeforces 1324C)
Logic:
1. To minimize the maximum jump distance, we find the largest gap 
   between any two 'R' positions.
2. The distance between 'R's at indices i and j is (j - i).
3. We include the start (0) and end (n+1) in our distance checks.

Complexity Analysis:
- Time: O(N) 
- Space: O(1)
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        s = input()
        n = len(s)

        # anchor = last available 'R' position (start at 0)
        anchor = 0
        max_gap = 0

        for i in range(n):
            if s[i] == 'R':
                # Calculate gap from previous 'R' to current 'R' (at i+1)
                max_gap = max(max_gap, (i + 1) - anchor)
                anchor = i + 1

        # Check the final gap to the destination (n + 1)
        max_gap = max(max_gap, (n + 1) - anchor)
        
        print(max_gap)

if __name__ == "__main__":
    solve()