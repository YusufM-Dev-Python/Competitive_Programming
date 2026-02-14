"""
Day 15: Candy Equalization (Codeforces 1490A Logic)
Problem Link: https://codeforces.com/contest/1490/problem/A

Logic:
To make all piles of candies equal using only the 'eat' operation (reduction), 
the final count for all piles must be equal to the smallest pile currently 
available. Any candy pile larger than the minimum must be reduced.
Total eaten = Sum of (each_pile - minimum_pile).

Complexity Analysis:
- Time: O(N) - One pass to find the minimum, one pass to calculate the sum.
- Space: O(N) - To store the input array.
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
        a = list(map(int, input().split()))
        
        # Step 1: Find the floor (the lowest value everyone must reach)
        target = min(a)
        
        # Step 2: Calculate the total 'distance' to the target
        eaten = 0
        for candy in a:
            eaten += (candy - target)
            
        print(eaten)

if __name__ == "__main__":
    solve()