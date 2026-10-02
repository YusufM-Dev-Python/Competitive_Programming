"""
Day 147: Codeforces 1559A - Mocha and Math
Topic: Bit Manipulation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements `arr`.
3. The operation allows replacing any $a_i$ and $a_j$ with $a_i \land a_j$. Since we can perform this operation any number of times in any order, we can effectively compute the bitwise AND of the entire array.
4. The minimum possible maximum element we can achieve is the bitwise AND of all elements in the array.
5. Compute the cumulative bitwise AND from the first element to the last and print the result.

Complexity Analysis:
- Time: O(N) per test case - single pass through the array to compute the bitwise AND.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ans = arr[0]
        for i in range(1, n):
            ans &= arr[i]

        print(ans)

if __name__ == "__main__":
    solve()