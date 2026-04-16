"""
Day 58: Optimized Scoring (1300 Rated Logic)
Logic:
1. Identify how many numbers are divisible by x, by y, and by both (LCM).
2. 'collision' count must be removed from both because they cancel out.
3. Use the Greedy approach:
   - Assign the largest available numbers to x-only indices.
   - Assign the smallest available numbers to y-only indices.
4. Use the Arithmetic Progression sum formula to calculate totals in O(1).

Complexity Analysis:
- Time: O(1) per test case (math formulas).
- Space: O(1).
"""

import sys
import math

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, x, y = map(int, input().split())

        # Find collisions using Least Common Multiple
        lcm_xy = math.lcm(x, y)
        collision = n // lcm_xy

        # Count how many unique positions each divisor has
        count_x = (n // x) - collision
        count_y = (n // y) - collision

        # Greedy: Give x the biggest numbers, give y the smallest
        # Sum of first 'count_y' integers: 1 + 2 + ... + count_y
        sum_y = count_y * (count_y + 1) // 2
        
        # Sum of last 'count_x' integers: (n) + (n-1) + ... + (n - count_x + 1)
        # Formula: (Number of terms / 2) * (First + Last)
        sum_x = count_x * (2 * n - count_x + 1) // 2

        print(sum_x - sum_y)

if __name__ == "__main__":
    solve()