"""
Day 82: Cyclic Shortest Distance (1100 Rated)
Topic: Graphs / Math / Shortest Path
Logic:
1. On a cycle of size 'n', the distance between two points x1 and x2 can be traversed in two ways:
   - Direct absolute difference: abs(x1 - x2)
   - Around the remaining loop of the cycle: n - abs(x1 - x2)
2. We take the minimum of these two paths to get the true shortest path on a circle.
3. If n <= 3, the constant 'k' modification is handled separately, otherwise we add 'k' 
   to the calculated minimum distance.

Complexity Analysis:
- Time: O(1) per test case - Basic constant time arithmetic operations.
- Space: O(1) - Only storing primitive integer tracking variables.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, x1, x2, k = map(int, input().split())
        time = 0

        # Calculate minimum distance on a circular layout
        if n <= 3:
            k = 0
            time = min(n - abs(x1 - x2), abs(x1 - x2)) + k
        else:
            time = min(n - abs(x1 - x2), abs(x1 - x2)) + k
        print(time)

if __name__ == "__main__":
    solve()