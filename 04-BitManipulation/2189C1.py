"""
Day 158: Codeforces 2189C1 - Permutation & Bitwise Observation
Topic: Bit Manipulation / Constructive / Permutations
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n`.
3. Initialize an answer array and a boolean tracking array (`used`) to manage unique elements from $1$ to $n$.
4. Leverage the key bitwise observation: XORing with `1` toggles the rightmost bit. Assign values utilizing `1 ^ i` for intermediate positions while marking them as used.
5. Fill in any remaining unused values for the remaining positions, and print the resulting permutation.

Complexity Analysis:
- Time: O(N) per test case - linear pass to assign values and find unused elements.
- Space: O(N) - to store the answer and `used` arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        ans = [0] * (n + 1)
        used = [False] * (n + 1)

        ans[n] = 1
        used[1] = True

        for i in range(2, n):
            ans[i] = 1 ^ i
            used[ans[i]] = True

        for v in range(1, n + 1):
            if not used[v]:
                ans[1] = v
                break

        print(*ans[1:])

if __name__ == '__main__':
    solve()