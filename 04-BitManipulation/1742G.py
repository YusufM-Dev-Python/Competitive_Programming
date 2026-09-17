"""
Day 136: Codeforces 1742G - Orray
Topic: Greedy / Bit Manipulation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements.
3. Greedily pick elements that maximize the bitwise OR sum at each step up to 30 iterations (since values fit in standard integer bits).
4. Keep track of used elements with a boolean array, append the best choice to the answer list, and update the current OR value.
5. Finally, append all remaining unused elements in their original relative order and print the result.

Complexity Analysis:
- Time: O(min(30, N) * N) per test case - finding the optimal next element iteratively.
- Space: O(N) - to store the array and tracking arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ans = []
        curr_or = 0
        max_or = 0

        used = [False] * (n)

        for step in range(min(30, n)):
            max_or = curr_or
            best_idx = -1

            for i in range(n):
                if not used[i]:
                    if (curr_or | arr[i]) > max_or:
                        max_or = curr_or | arr[i]
                        best_idx = i

            if best_idx == -1:
                break

            used[best_idx] = True
            ans.append(arr[best_idx])
            curr_or = max_or

        for i in range(n):
            if not used[i]:
                ans.append(arr[i])

        print(*ans)

if __name__ == '__main__':
    solve()