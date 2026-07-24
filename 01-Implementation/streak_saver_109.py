"""
Day 109: Streak Saver - Basic Construction
Topic: Implementation
Goal: Output sequential values up to 'n' for each test case.

Logic:
1. Read the number of test cases 't'.
2. For each test case, read 'n' and print numbers from 1 to 'n' sequentially.
3. Serves as a straightforward pattern or template construction script to maintain 
   daily consistency.

Complexity Analysis:
- Time: O(N) per test case - Linear print loop up to n.
- Space: O(1) - Constant auxiliary space.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())

        # Simple sequential loop
        for i in range(n):
            print(i + 1)

if __name__ == "__main__":
    solve()