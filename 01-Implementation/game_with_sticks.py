"""
Day 20: Game With Sticks (Codeforces 451A)
Problem Link: https://codeforces.com/contest/451/problem/A

Logic:
Two players remove sticks by picking an intersection. 
- Picking an intersection point (x, y) removes the entire x-th row and y-th column.
- This means every move reduces the available rows by 1 and available columns by 1.
- The game ends when either rows or columns reach 0.
- The total number of moves possible is min(n, m).

Akshat goes first (Move 1, 3, 5...).
Malvika goes second (Move 2, 4, 6...).

Complexity Analysis:
- Time: O(1) - Simple comparison and modulo check.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read n (rows) and m (columns)
    line = input().split()
    if not line: return
    n, m = map(int, line)

    # The game ends after min(n, m) turns
    total_turns = min(n, m)

    # Akshat wins on odd turns, Malvika on even
    if total_turns % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")

if __name__ == "__main__":
    solve()