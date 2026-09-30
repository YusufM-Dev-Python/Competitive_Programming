"""
Day 145: Codeforces 1481B - New Colony
Topic: Simulation / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each testcase, read `n` (number of boulders/heights) and `k` (the boulder number we want to track).
3. Simulate dropping each of the `k` boulders one by one. Each boulder rolls from the start (`curr = 0`) until it either finds a step where it can rest (height increases, so we increment that height and break) or reaches the end (`curr == n-1`), meaning it falls off.
4. Track the position where the $k$-th boulder rests. If it falls off before reaching $k$ boulders, print `-1`. Otherwise, print the 1-indexed final resting position.

ComplexityAnalysis:
- Time: O(K * N) per test case - simulating each of the K boulders rolling across N heights.
- Space: O(N) - to store the heights array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        h = list(map(int, input().split()))

        pos = -1
        fell = False

        for _ in range(k):
            curr = 0
            while curr < n - 1:
                if h[curr] >= h[curr+1]:
                    curr += 1
                else:
                    h[curr] += 1
                    break

            if curr == n - 1:
                fell = True
                break
            else:
                pos = curr + 1

        if fell:
            print(-1)
        else:
            print(pos)
        
if __name__ == "__main__":
    solve()