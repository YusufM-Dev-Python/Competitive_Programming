"""
Day 155: Codeforces 2271B - Frequency Counting & Condition Checks
Topic: Implementation / Frequency Arrays
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`, followed by the array elements `arr`.
3. Use a frequency array (`count`) of size `n + 1` to record occurrences of each element.
4. Iterate through counts to verify if the required thresholds (based on $2k$) are met to determine the output ("YES" or "NO").
5. Print the final answer for each test case.

Complexity Analysis:
- Time: O(N) per test case - single pass for frequency counting and linear scan for condition validation.
- Space: O(N) - to store the frequency array and input list.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        count = [0] * (n + 1)

        for x in arr:
            count[x] += 1

        ans = "NO"
        for i in range(n):
            if count[i] < 2 * k:
                if count[i] == 2 * k - 1:
                    ans = "YES"
                break
        print(ans)        

if __name__ == "__main__":
    solve()