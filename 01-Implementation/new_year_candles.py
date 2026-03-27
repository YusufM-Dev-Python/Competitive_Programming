"""
Day 41: New Year Candles (Codeforces 379A)
Problem Link: https://codeforces.com/contest/379/problem/A

Logic:
1. Start with 'a' candles. Each provides 1 hour of light and 1 unit of wax.
2. Total hours = 'a'. Initial leftovers = 'a'.
3. While we have enough leftovers to make at least one new candle (leftover >= b):
   - New candles = leftover // b.
   - Add these to total hours.
   - New leftover = (newly created candles) + (remainder wax that couldn't make a candle).

Complexity Analysis:
- Time: O(log_b A) - The number of candles decreases geometrically.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input().split()
    if not line: return
    a, b = map(int, line)

    hours = a
    leftover = a

    # Simulation loop
    while leftover // b != 0:
        new_candles = leftover // b
        hours += new_candles
        # The new wax comes from the candles we just burned 
        # plus whatever was left over from the previous recycling
        leftover = new_candles + (leftover % b)

    print(hours)    

if __name__ == "__main__":
    solve()