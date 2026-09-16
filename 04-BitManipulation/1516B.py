"""
Day 135: Codeforces 1516B - AGAGA XOOORRR
Topic: Bit Manipulation / Greedy / Prefix XOR
Logic:
1. Read the number of test cases `t`.
2. For each test case, compute the total XOR sum of the entire array (`total_xor`).
3. If `total_xor` is 0, we can always split the array into two equal XOR parts, so print "YES".
4. Otherwise, check if we can partition the array into 3 or more segments such that each segment has an XOR sum equal to `total_xor`. We scan through the array maintaining a `running_xor` and count how many such segments we can form. If `count >= 3`, print "YES", else "NO".

Complexity Analysis:
- Time: O(N) per test case - single pass to find the total XOR and another pass to check segments.
- Space: O(N) - to store the array elements.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        total_xor = 0

        for i in range(n):
            total_xor ^= arr[i]

        if total_xor == 0:
            print("YES")
            continue

        count = 0
        running_xor = 0
        possible = False
        for i in range(n):
            running_xor ^= arr[i]
            if running_xor == total_xor:
                count += 1
                running_xor = 0
            if count == 3:
                possible = True
                break

        print("YES") if possible else print("NO")

if __name__ == "__main__":
    solve()