"""
Day 157: Codeforces 2276C - Prefix Sums Modulo K & Frequency Tracking
Topic: Prefix Sums / Modular Arithmetic / Hash Maps
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`, followed by the array elements `arr`.
3. Compute prefix sum remainders modulo `k` and store them in `pf`.
4. Maintain a frequency dictionary to track valid remainders conforming to the range constraints dictated by `k`.
5. Iterate through possible right boundaries `r`, updating frequency counts and accumulating the matching pairs into `ans`.

Complexity Analysis:
- Time: O(N) per test case - optimal linear pass with dictionary lookups and prefix sums.
- Space: O(N) - to store prefix sum arrays and frequency maps.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        pf = [0] * (n + 1)

        for i in range(n):
            pf[i + 1] = (pf[i] + arr[i]) % k

        freq = {}

        ans = 0

        for r in range(k + 1, n + 1):
            j = r - k - 1
            if j >= 0:
                rem = pf[j]
                freq[rem] = freq.get(rem, 0) + 1

            current_rem = pf[r]
            if current_rem in freq:
                ans += freq[current_rem]

        print(ans)

if __name__ == "__main__":
    solve()