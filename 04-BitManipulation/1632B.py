"""
Day 151: Codeforces 1632B - Find the Array / Bitwise Observation
Topic: Bit Manipulation / Greedy / Constructive
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n`.
3. Find the largest power of 2 strictly less than `n` (let's call it `k`). 
4. Placing elements from `1` to `k-1` followed by `0`, and then from `k` to `n-1` ensures that the single large XOR jump involving the most significant bit happens across just one boundary (between `0` and `k`), minimizing the maximum adjacent XOR sum.
5. Print the constructed array.

Complexity Analysis:
- Time: O(N) per test case - generating and printing the array elements.
- Space: O(N) - to store the array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []

        k = 1
        while k * 2 < n:
            k *= 2

        for i in range(1, k):
            arr.append(i)

        arr.append(0)

        for i in range(k, n):
            arr.append(i)

        print(*arr)

if __name__ == "__main__":
    solve()