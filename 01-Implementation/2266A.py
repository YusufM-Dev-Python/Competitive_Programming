"""
Day 139: Codeforces 2266A - Contest Problem / Implementation
Topic: Greedy / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements.
3. Compute the result by finding the difference between `n` and the minimum element in the array (`n - min(arr)`).
4. Print the result for each testcase.

Complexity Analysis:
- Time: O(N) per test case - finding the minimum element in the array of size N.
- Space: O(N) - to store the array elements.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        print(n - min(arr))

if __name__ == '__main__':
    solve()