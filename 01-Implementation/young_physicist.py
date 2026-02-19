"""
Day 19: Young Physicist (Codeforces 69A)
Problem Link: https://codeforces.com/contest/69/problem/A

Logic:
This is a problem of 3D Vector Addition. For a body to be in equilibrium:
- The sum of all force components along the X-axis must be 0.
- The sum of all force components along the Y-axis must be 0.
- The sum of all force components along the Z-axis must be 0.

If any of these sums are non-zero, the body is moving.

Complexity Analysis:
- Time: O(N) - We iterate through the N vectors once.
- Space: O(1) - We only store three integer counters regardless of N.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read the number of vectors
    n_str = input()
    if not n_str: return
    n = int(n_str)
    
    # Initialize 'buckets' for each dimension
    x_sum = 0
    y_sum = 0
    z_sum = 0
    
    for _ in range(n):
        # Read components for the current vector
        x, y, z = map(int, input().split())
        x_sum += x
        y_sum += y
        z_sum += z
        
    # Equilibrium requires all independent sums to be zero
    if x_sum == 0 and y_sum == 0 and z_sum == 0:
        print('YES')
    else:
        print("NO")

if __name__ == "__main__":
    solve()