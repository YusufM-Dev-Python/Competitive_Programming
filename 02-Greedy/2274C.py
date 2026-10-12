"""
Day 156: Codeforces 2274C - Greedy Construction / Simulation
Topic: Greedy / Simulation / Number Theory
Logic:
1. Read the number of test cases `t`.
2. For each test case, read integer `n`.
3. Use a greedy loop to find the minimum cost `k` such that the cumulative value meets or exceeds `n`.
4. Construct the bag allocation sequence in reverse order from `cost` down to `1`, updating remaining quantities and expanding bags accordingly.
5. Print the total cost and the constructed array.

Complexity Analysis:
- Time: O(K^2 + N) per test case - depending on the magnitude of `k` and sequence generation.
- Space: O(N) - to store the answer array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        cost = 0 

        k = 1
        while True:
            total = 0
            for i in range(1, k + 1):
                total += (k // i) * i
            if total >= n:
                cost = k
                break
            k += 1

        bags = 1
        rem = n
        ans = []

        for i in range(cost, 0, -1):
            count = min(cost // i, rem // i)
            for _ in range(count):
                ans.extend([bags] * i)
                bags += 1

            rem -= count * i

        print(cost)
        print(*ans)

if __name__ == "__main__":
    solve()