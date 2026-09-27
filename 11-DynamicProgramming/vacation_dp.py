"""
Day 142: Mock ICPC / Contest - Vacation DP
Topic: Dynamic Programming
Logic:
1. Read the number of test cases `t` (or days `n`).
2. For each day, read three cost/point arrays `a`, `b`, and `c` corresponding to three available activities.
3. Use a 2D DP table `dp[i][j]` where `i` represents the day and `j` represents the chosen activity (0, 1, or 2), ensuring we don't choose the same activity on consecutive days.
4. Transition by taking the maximum of the other two choices from the previous day.
5. Print the maximum points achievable on the final day.

Complexity Analysis:
- Time: O(N) per test case - iterating through the days once with constant transitions.
- Space: O(N) - to store the DP table and activity arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        

        dp = [[0] * 3 for _ in range(n)]

        dp[0][0] = a[0]
        dp[0][1] = b[0]
        dp[0][2] = c[0]

        for i in range(1, n):
            dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2])
            dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2])
            dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1])

        ans = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
        print(ans)

if __name__ == "__main__":
    solve()