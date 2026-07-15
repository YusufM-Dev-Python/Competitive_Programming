"""
Day 100 (Final): 2244C - Number Theory/GCD Constraint
Topic: Math / Number Theory
Logic:
1. The condition for the sequence relates to the difference between elements 
   and their indices, specifically modular arithmetic with the GCD of x and y.
2. If (p[i] - (i + 1)) is not divisible by gcd(x, y) for any element, 
   the condition cannot be satisfied ("NO").
3. Otherwise, the condition holds ("YES").

Complexity Analysis:
- Time: O(N + log(min(x, y))) per test case.
- Space: O(N) to store the array.
"""

import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n, x, y = map(int, input().split())
        p = list(map(int, input().split()))

        gc = math.gcd(x, y)
        possible = True
        
        # Check if every element satisfies the GCD-based modular condition
        for i in range(n):
            if (p[i] - (i + 1)) % gc != 0:
                possible = False
                break
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    solve()