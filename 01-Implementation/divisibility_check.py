"""
Day 88: Divisibility Check
Topic: Math / Number Theory
Logic:
1. The problem asks whether a number x can be perfectly divided by y without leaving a remainder.
2. We utilize the modulo operator (x % y). If the result is 0, it means x is a multiple of y, so we output "YES".
3. Otherwise, we output "NO".

Complexity Analysis:
- Time: O(1) per test case - Basic constant time arithmetic modulo operation.
- Space: O(1) - Primitive integers only.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())

        # Check if x is completely divisible by y
        if x % y == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()