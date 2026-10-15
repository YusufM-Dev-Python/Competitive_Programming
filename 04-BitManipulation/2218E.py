"""
Day 158: Codeforces 2218E - Maximum XOR Pair Search
Topic: Bit Manipulation / Brute Force / Optimization
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n` and the array elements `arr`.
3. Compute the bitwise XOR for pairs of elements to find the maximum possible XOR result.
4. Print the maximum XOR value found.

Complexity Analysis:
- Time: O(N^2) per test case - nested loops comparing array elements.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        max_ans = 0
        curr_ans = 0

        for i in range(n):
            for j in range(1, n):
                curr_ans = arr[i] ^ arr[j]
                max_ans = max(curr_ans, max_ans)

        print(max_ans)

if __name__ == "__main__":
    solve()