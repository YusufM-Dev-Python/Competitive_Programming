"""
Day 159: Codeforces 2261A - String Bounds / Index Tracking
Topic: Strings / Implementation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read string length `n` and the string `s`.
3. Track the total count of '1's along with their first and last occurrence indices.
4. Handle cases based on the count: if 1, output 0; if 2, output 1; otherwise, compute the span distance `last_idx - first_idx`.

Complexity Analysis:
- Time: O(N) per test case - single pass through the string.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        first_idx = -1
        last_idx = -1
        cnt = 0

        for i in range(n):
            if s[i] == '1':
                cnt += 1
                if first_idx == -1:
                    first_idx = i
                last_idx = i

        if cnt == 1:
            print(0)
        elif cnt == 2:
            print(1)
        else:
            print(last_idx - first_idx)

if __name__ == "__main__":
    solve()