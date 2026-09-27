"""
Day 142: Mock ICPC - Luminara Night Festival Shuttle Stops
Topic: Greedy / Array Manipulation
Logic:
1. Read the number of stops `n` and the sorted list of stop positions `arr`.
2. Compute the gaps between every pair of consecutive stops.
3. Track the two largest gaps (`max_gap` and `second_max_gap`) in a single pass.
4. The optimal strategy to minimize the maximum gap after adding one new stop is to split the single largest gap roughly in half: `(max_gap + 1) // 2`.
5. The answer is the maximum between this split gap and the `second_max_gap` (since the other gaps remain unchanged). Print the result.

Complexity Analysis:
- Time: O(N) - single pass to compute adjacent gaps and track the top two.
- Space: O(N) - to store the stop positions array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    max_gap = 0
    second_max_gap = 0

    for i in range(1, n):
        gap = arr[i] - arr[i - 1]
        if gap > max_gap:
            second_max_gap = max_gap
            max_gap = gap
        elif gap > second_max_gap:
            second_max_gap = gap

    ans = max(second_max_gap, (max_gap + 1) // 2)
    print(ans)

if __name__ == "__main__":
    solve()