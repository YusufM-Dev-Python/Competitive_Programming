"""
Day 141: Codeforces 2269A - Math / Implementation
Topic: Math / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`.
3. Compute the waiting count (`wait = n - k + 1`) and the remaining count (`left = n - wait`).
4. Calculate the result using the formula `2**(wait) + 2*left` and print it.

Complexity Analysis:
- Time: O(1) per test case - constant time arithmetic operations.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        wait = n - k + 1
        left = n - wait

        print(2**(wait) + 2*left)
        
if __name__ == "__main__":
    solve()