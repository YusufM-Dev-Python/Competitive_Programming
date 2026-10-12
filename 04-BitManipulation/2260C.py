"""
Day 156: Codeforces 2260C - Submask Optimization / Bit Manipulation
Topic: Bit Manipulation / Greedy Submask Construction
Logic:
1. Read the number of test cases `t`.
2. For each test case, read inputs `x` and `y`, and compute their sum `s = x + y`.
3. Iterate through bits from position `30` down to `0` to construct the submask `xp` greedily:
   - Once a `free` flag is triggered (when bit conditions allow full flexibility), subsequent bits can directly take the value from `s`.
   - Otherwise, compare individual bits of `x` and `s` to determine whether to set the bit or activate the `free` state.
4. Print the sum `s` and the resulting difference `x - xp`.

Complexity Analysis:
- Time: O(1) per test case - fixed 31 iterations for bitwise checks.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())

        s = x + y
        xp = 0
        free = False

        for i in range(30, -1, -1):
            xb = (x >> i) & 1
            sb = (s >> i) & 1

            if free:
                xp |= (sb << i)
            elif xb == 1 and sb == 1:
                xp |= 1 << i          
            elif xb == 0 and sb == 0:
                xp |= 0 << i                
            elif xb == 0 and sb == 1:
                xp |= 0 << i                
            elif xb == 1 and sb == 0:
                free = True 

        print(f"{s} {x - xp}")

if __name__ == "__main__":
    solve()