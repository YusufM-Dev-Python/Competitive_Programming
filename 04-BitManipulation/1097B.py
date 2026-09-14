"""
Day 134: Codeforces 1097B - Petr and a Combination Lock
Topic: Brute Force / Bitmasking
Logic:
1. Read the number of rotations `n` and the angles array `arr`.
2. Use bitmasking from `0` to `2^n - 1` to represent all possible choices of adding or subtracting each angle (e.g., rotating clockwise or counterclockwise).
3. For each mask, compute the final angle sum. If the sum is divisible by 360 (`ans % 360 == 0`), a valid combination is found.
4. Print "YES" if a valid configuration exists, otherwise "NO".

Complexity Analysis:
- Time: O(N * 2^N) - Evaluating all 2^n subsets, each taking O(N) operations. (Given N is small, usually N <= 15, this easily passes).
- Space: O(N) - To store the angles array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        num = int(input())
        arr.append(num)
    possible = False

    for mask in range(0, 2**n):
        ans = 0
        for i in range(n):
            if ((mask >> i) & 1) == 1:
                ans += arr[i]
            else:
                ans -= arr[i]

        if ans % 360 == 0:
            possible = True
            break

    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()