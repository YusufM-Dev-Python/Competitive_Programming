"""
Day 157: Codeforces 2276B - String Pattern Matching
Topic: Strings / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read string `s` and compute its length `n`.
3. Initialize pattern flags (`short`, `long`) to false.
4. Iterate through the string from index `1` to `n - 2`, checking neighboring character relations (`s[i-1] == s[i+1]`) to classify matching structural patterns.
5. Compute and print the final result based on active pattern flags.

Complexity Analysis:
- Time: O(N) per test case - single linear scan through the string length.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)

        short = False
        long = False

        for i in range(1, n - 1):
            if s[i-1] == s[i+1]:
                if s[i] == s[i-1]:
                    long = True
                else:
                    short = True
        print(1 + short + long)

if __name__ == "__main__":
    solve()