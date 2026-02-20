"""
Day 20: Lucky Division (Codeforces 122A)
Problem Link: https://codeforces.com/contest/122/problem/A

Logic:
A number is 'almost lucky' if it's divisible by a lucky number.
Lucky numbers are those that contain only digits 4 and 7.
Given n <= 1000, we can simply pre-define all lucky numbers up to 1000
and check if n is divisible by any of them.

Lucky numbers <= 1000:
4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777.

Complexity Analysis:
- Time: O(1) - Testing divisibility against a small fixed list.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_str = input()
    if not n_str: return
    n = int(n_str)

    # All lucky numbers up to 1000
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    # Check if n is almost lucky
    is_almost_lucky = False
    for lucky in lucky_numbers:
        if n % lucky == 0:
            is_almost_lucky = True
            break
    
    if is_almost_lucky:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()