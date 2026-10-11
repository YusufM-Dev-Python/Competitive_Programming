"""
Day 155: Codeforces 2217A - Parity Validation / Math
Topic: Implementation / Parity Analysis
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`, followed by the array elements `arr`.
3. Compute the total sum of the array (`sum_ans`).
4. Apply the parity constraint: if the total sum is even while the product `n * k` is odd, it's impossible to satisfy the condition, so print "NO". Otherwise, print "YES".

Complexity Analysis:
- Time: O(N) per test case - linear pass to compute the array sum.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        sum_ans = sum(arr)

        if sum_ans % 2 == 0 and (n * k) % 2 != 0:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve()