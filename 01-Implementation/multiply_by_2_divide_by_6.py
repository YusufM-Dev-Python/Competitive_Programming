"""
Day 29: Multiply by 2, divide by 6 (Codeforces 1374B)
Problem Link: https://codeforces.com/contest/1374/problem/B

Logic:
1. We want to reach 1 using two operations: n * 2 or n / 6.
2. Notice n / 6 = n / (2 * 3).
3. To reach 1, n must only have prime factors 2 and 3.
4. Furthermore, the exponent of 3 must be >= the exponent of 2.
5. Each multiplication by 2 adds a '2' factor. 
6. Each division by 6 removes one '2' and one '3'.

Complexity Analysis:
- Time: O(log N) - Each step significantly reduces n or prepares it for reduction.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        steps = 0

        # Simulation approach
        while n > 1:
            if n % 6 == 0:
                n //= 6
                steps += 1
            elif n % 3 == 0:
                # If divisible by 3 but not 6, we must multiply by 2 
                # to create a multiple of 6.
                n *= 2
                steps += 1
            else:
                # If not divisible by 3, we can never reach 1
                break
        
        if n == 1:
            print(steps)
        else:
            print("-1")
            
if __name__ == "__main__":
    solve()