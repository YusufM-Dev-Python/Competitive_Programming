"""
Day 159: Codeforces 2261C - Parity State Analysis
Topic: Implementation / Parity Counting
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array `a`.
3. Count the total number of even (`evens`) and odd (`odds`) elements in the array.
4. Apply specific parity conditions: if `(evens == 1 and odds == 1)` or `(evens == 0 and odds == 3)`, print "Larpity"; otherwise, print "Moggity".

Complexity Analysis:
- Time: O(N) per test case - single pass through the array to count parities.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        odds = 0
        evens = 0

        for i in range(n):
            if a[i] % 2 == 0:
                evens += 1
            else:
                odds += 1

        if (evens == 1 and odds == 1) or (evens == 0 and odds == 3):
            print("Larpity")
        else:
            print("Moggity")

if __name__ == "__main__":
    solve()