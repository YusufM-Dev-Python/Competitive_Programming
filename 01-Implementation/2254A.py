"""
Day 119: 2254A - Contest Simulation
Topic: Implementation / Simulation
Goal: Simulate rounds of adjustments between three variables until two or more become equal.

Logic:
1. Loop Condition: Continue simulation as long as all three variables (`a`, `b`, `c`) are distinct.
2. Relative Ordering: Check all permutations of relative sizes (`a > b > c`, `a > c > b`, etc.).
3. State Transition: Increment the round count while decrementing the largest element 
   and incrementing the appropriate smaller element based on the active ordering condition.

Complexity Analysis:
- Time: Depends on the magnitude of differences between variables, efficiently simulated step by step.
- Space: O(1) - Constant space variables.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        a, b, c = map(int, input().split())

        rounds = 0

        # Simulate rounds while all three values are distinct
        while a != b and a != c and b != c:
            if a > b > c:
                a -= 1
                c += 1
                rounds += 1
            elif a > c > b:
                a -= 1
                b += 1
                rounds += 1
            elif b > a > c:
                b -= 1
                c += 1
                rounds += 1
            elif b > c > a:
                b -= 1
                a += 1
                rounds += 1
            elif c > a > b:
                c -= 1
                b += 1
                rounds += 1
            elif c > b > a:
                c -= 1
                a += 1
                rounds += 1

        print(rounds)

if __name__ == "__main__":
    solve()