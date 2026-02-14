"""
Day 15: Word on the Paper (Codeforces 1850C)
Problem Link: https://codeforces.com/contest/1850/problem/C

Logic:
We are given an 8x8 grid of dots (.) and lowercase Latin letters. The letters 
form a single word spelled vertically from top to bottom. Because we read 
the grid row by row, we will naturally encounter the letters in their 
correct vertical order. We simply filter out the dots and keep the letters.

Complexity Analysis:
- Time: O(1) - The grid size is fixed at 8x8 (64 operations per test case).
- Space: O(1) - We only store the characters of the resulting word.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        chars = []
        # The grid is always 8x8
        for _ in range(8):
            row = input()
            for char in row:
                # If it's not a dot, it's part of our hidden word
                if char != '.':
                    chars.append(char)
        
        # Combine the characters into the final word
        print("".join(chars))

if __name__ == "__main__":
    solve()