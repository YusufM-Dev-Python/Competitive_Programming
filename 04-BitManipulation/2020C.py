"""
Day 150: Codeforces 2020C - Bitwise Equation
Topic: Bit Manipulation / Bitwise Operations
Logic:
1. Read the number of test cases `t`.
2. For each test case, read inputs `b`, `c`, and `d`.
3. Since bitwise operations are independent across each bit position, solve for bit `i` from `0` to `60` independently.
4. Extract the $i$-th bit for `b`, `c`, and `d`. Test both possible values of `ai` (0 or 1) to see if `(ai | bi) - (ai & ci) == di` holds true.
5. If a valid `ai` is found, add it to our answer `a` at the correct bit shift. If no valid bit can satisfy the equation for any position, print `-1`. Otherwise, print `a`.

Complexity Analysis:
- Time: O(1) per test case - fixed 61 iterations regardless of input size.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        b, c, d = map(int, input().split())

        a = 0        
        done = False

        for i in range(61):
            bi = (b >> i) & 1
            ci = (c >> i) & 1
            di = (d >> i) & 1

            found = False
            for ai in (0, 1):
                if (ai | bi) - (ai & ci) == di:
                    a += (ai << i)
                    found = True
                    break

            if not found:  
                done = True
                break

        print(-1 if done else a)

if __name__ == "__main__":
    solve()