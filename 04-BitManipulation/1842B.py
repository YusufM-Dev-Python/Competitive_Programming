"""
Day 138: Codeforces 1842B - Tenzing and Books
Topic: Bit Manipulation / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the target knowledge `x`, followed by three arrays representing books on three stacks (`a`, `b`, and `c`).
3. Traverse through each stack from top to bottom as long as the books can be included without introducing any bits not present in `x` (i.e., `(val | x) == x`).
4. Accumulate the bitwise OR sum of the readable books from each stack into `k1`, `k2`, and `k3`.
5. Check if the combined OR sum of all chosen books equals `x`. If `(k1 | k2 | k3) == x`, print "YES", otherwise "NO".

Complexity Analysis:
- Time: O(N) per test case - iterating through the three lists at most once.
- Space: O(N) - to store the arrays for the three book stacks.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))

        k1 = 0
        k2 = 0
        k3 = 0

        i = 0
        while i != n:
            if (a[i] | x) != x:
                break
            else:
                k1 |= a[i]
            i += 1

        i = 0
        while i != n:
            if (b[i] | x) != x:
                break
            else:
                k2 |= b[i]
            i += 1

        i = 0
        while i != n:
            if (c[i] | x) != x:
                break
            else:
                k3 |= c[i]
            i += 1

        if (k1 | k2 | k3) == x:
            print("YES")
        else:
            print("NO") 

if __name__ == "__main__":
    solve()