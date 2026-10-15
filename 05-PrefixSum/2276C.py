"""
Day 157: Codeforces 2276C - Prefix Sums Modulo K (Array-Based Frequency Optimization)
Topic: Prefix Sums / Modular Arithmetic / Frequency Array
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`, followed by the array elements `arr`.
3. Compute prefix sum remainders modulo `k` and store them in `pf`.
4. Instead of a Python dictionary (which can trigger TLE or hash collisions), use a fixed-size frequency array `freq = [0] * k` since all remainders are strictly less than `k`.
5. Maintain the sliding window boundaries, increment remainder counts in the frequency array, and accumulate matching pairs into `ans` in O(1) time per step.

Complexity Analysis:
- Time: O(N) per test case - optimal linear pass with direct array indexing instead of hash map overhead.
- Space: O(N + K) - to store prefix sums and the frequency count array of size `k`.
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

        freq = [0] * k

        ans = 0

        for r in range(k + 1, n + 1):
            j = r - k - 1
            if j >= 0:
                rem = pf[j]
                freq[rem] += 1

            current_rem = pf[r]
            ans += freq[current_rem]

        print(ans)

if __name__ == "__main__":
    solve()