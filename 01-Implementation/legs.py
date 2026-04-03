"""
Day 46: Legs (Codeforces 1996A)
Problem Link: https://codeforces.com/contest/1996/problem/A

Logic:
1. We want to minimize the total number of animals (cows + chickens).
2. Cows have 4 legs, chickens have 2.
3. Greedy choice: Use as many cows as possible.
4. Total animals = (n // 4) + (remaining legs // 2).

Complexity Analysis:
- Time: O(T) where T is the number of test cases.
- Space: O(1).
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_line = input()
    if not t_line: return
    t = int(t_line)
    
    for _ in range(t):
        n_line = input()
        if not n_line: continue
        n = int(n_line)
        
        # Maximize cows (4 legs), then use chickens (2 legs) for the rest
        ans = (n // 4) + (n % 4 // 2)
        print(ans)

if __name__ == "__main__":
    solve()