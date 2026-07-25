"""
Day 110: 2184A - Parity and Base Case Optimization
Topic: Implementation / Math
Goal: Determine the outcome for a given integer 'n' based on specific modulo and base case rules.

Logic:
1. Base Cases: If n is 2 or 3, the special constraints of the problem return 'n' directly.
2. Even Check: If n is even (and greater than 2), it can be evenly reduced or partitioned, resulting in 0.
3. Odd Check: For other odd numbers greater than 3, the remainder/result yields 1.
4. This allows us to bypass heavy simulation and solve each test case in O(1) time.

Complexity Analysis:
- Time: O(1) per test case - Constant time conditional checks.
- Space: O(1) - No extra data structures required.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())

        # Base cases
        if n == 2 or n == 3:
            print(n)
        # Even numbers partition cleanly
        elif n % 2 == 0:
            print(0)
        # Remaining odd numbers
        else:
            print(1)

if __name__ == '__main__':
    solve()