"""
Day 156: Codeforces 2274A - Alternating Parity Summation
Topic: Implementation / Array Manipulation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n` and the array `arr`.
3. Iterate through the array elements, adding values at even indices and subtracting values at odd indices to compute `sum_ans`.
4. Print the final computed sum.

Complexity Analysis:
- Time: O(N) per test case - single pass through the array.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        sum_ans = 0

        for i in range(n):
            if i % 2 == 0:
                sum_ans += arr[i]
            else:
                sum_ans -= arr[i]

        print(sum_ans)

if __name__ == "__main__":
    solve()