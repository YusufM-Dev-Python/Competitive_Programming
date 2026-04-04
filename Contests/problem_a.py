"""
Day 47: Codeforces Round 1090 (Div. 4) - Problem A
Problem Link: (Pending Official Name/Link)

Logic:
1. Read the input value x.
2. If x is below a certain threshold (67), increment it to ensure 
   the output meets the problem's specific constraints.
3. Otherwise, output x as is.
4. This is a common pattern for "A" problems where any valid 
   integer within a range works.

Complexity Analysis:
- Time: O(T) where T is the number of test cases.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        x_str = input()
        if not x_str: continue
        x = int(x_str)
        
        # Simple conditional manipulation to satisfy problem constraints
        if x < 67:
            y = x + 1
            print(y)
        else:
            print(x)

if __name__ == "__main__":
    solve()