"""
Day 105 (Part 2): 2225A - Basic Conditional Check
Topic: Implementation
Goal: Determine if a specific relationship between 'x' and 'y' satisfies the 
      condition for a valid output.

Logic:
1. The problem defines a forbidden state: whenever the relationship x * 2 == y 
   holds, the condition is not met.
2. In all other scenarios, the condition is met.
3. This is a direct implementation of the problem's base constraint.

Complexity Analysis:
- Time: O(1) - Constant time arithmetic check per test case.
- Space: O(1) - No extra storage required.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        x, y = map(int, input().split())

        # Simple conditional check as per the problem's constraint
        if x * 2 == y:
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    solve()