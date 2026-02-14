"""
Day 15: 1D Eraser (Codeforces 1873B)
Problem Link: https://codeforces.com/contest/1873/problem/B

Logic:
This is a Greedy approach. We want to cover all 'B' (black) cells using the 
minimum number of operations of length 'k'. 
- We scan the string from left to right.
- The moment we hit a 'B', we MUST use an operation.
- Since one operation covers 'k' consecutive cells, we simply skip the 
  next 'k' indices because they are now guaranteed to be 'W' (white).

Complexity Analysis:
- Time: O(N) - We visit each character at most once.
- Space: O(N) - To store the input string.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        # n: length of string, k: eraser power
        n, k = map(int, input().split())
        s = input()
        
        i = 0
        ops = 0
        
        # We use a while loop so we can 'jump' the index i
        while i < n:
            if s[i] == 'B':
                # Found a black cell, use the eraser
                ops += 1
                # Everything in the range [i, i+k-1] is now white
                i += k
            else:
                # Already white, just move to the next cell
                i += 1
                
        print(ops)

if __name__ == "__main__":
    solve()