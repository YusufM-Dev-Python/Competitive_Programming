"""
Day 25: Move Brackets (Codeforces 1374C)
Problem Link: https://codeforces.com/contest/1374/problem/C

Logic:
1. We track the 'balance' of brackets: +1 for '(' and -1 for ')'.
2. A sequence is only invalid if the balance drops below 0 at any point.
3. Every time bal < 0, it means we have a ')' that doesn't have a matching '('.
4. Instead of actually moving it, we increment our step counter and reset 
   the balance to 0, effectively 'moving' that bracket to the end.

Complexity Analysis:
- Time: O(N) - Single pass through the string.
- Space: O(N) - To store the input string.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())
        arr = input()

        bal = 0
        steps = 0
        for i in range(n):
            if arr[i] == '(':
                bal += 1
            elif arr[i] == ')':
                bal -= 1
            
            # If balance is negative, we have an unmatched closing bracket
            if bal < 0:
                steps += 1
                # Reset balance as if we moved this ')' to the end
                bal = 0
                
        print(steps)
            
if __name__ == "__main__":
    solve()