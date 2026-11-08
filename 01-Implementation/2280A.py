"""
Day 169: Codeforces 2280A - Are They the Same?
Topic: Parity Analysis / Modular Arithmetic / Transformations
Question Extraction:
- We are given two integer arrays `a` and `b`, each of length `n`, along with an integer `k`.
- We can perform operations zero or more times: a[i] := 2 * a[i] + k, a[i] := a[i] + 2, or a[i] := a[i] - 2.
- We need to determine if `a` can be transformed into a permutation of `b`.

Why we did this (Approach & Intuition):
- The allowed operations (adding/subtracting 2 and scaling/shifting with 2 * a[i] + k) preserve certain parity invariants depending on whether `k` is even or odd.
- By counting the distribution of evens and odds in both arrays `a` and `b`, we can determine whether the necessary parity constraints are satisfied for a valid transformation mapping.
- If `k` is even, the even-odd counts must align based on even transitions; if `k` is odd, the odd counts govern feasibility.

Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n`, `k`, and arrays `a` and `b`.
3. Count the number of even and odd elements in both `a` and `b` (`even_a`, `odd_a`, `even_b`, `odd_b`).
4. Check parity conditions based on whether `k` is even or odd, printing "YES" if valid or "NO" otherwise.

Complexity Analysis:
- Time: O(N) per test case - linear pass to count parities in both arrays.
- Space: O(N) to store input arrays `a` and `b`.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        even_a = 0
        odd_a = 0
        odd_b = 0
        even_b = 0

        for i in a:
            if i % 2 == 0:
                even_a += 1
            else:
                odd_a += 1

        for i in b:
            if i % 2 == 0:
                even_b += 1
            else:
                odd_b += 1

        if k % 2 == 0:
            if even_a <= even_b:
                print("YES")
            else:
                print("NO")
        else:
            if odd_a <= odd_b:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()