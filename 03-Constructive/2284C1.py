"""
Day 169: Codeforces 2284C1 - Constructive Disgusting Array Elimination (Easy Version)
Topic: Number Theory / Sieve / Prime Mapping / Constructive
Question Extraction:
- An array `b` is called disgusting if there exist indices i < j such that 1 < gcd(b_i, b_j) < min(b_i, b_j)[cite: 14].
- We are given an array `a` of length `n` and want to make it not disgusting by increasing elements subject to operations (gcd(a_i, x) = 1, incrementing a_i by x)[cite: 14].
- We need to find any valid array `b` obtainable under the allowed operations and restrictions[cite: 14].

Why we did this (Approach & Intuition):
- To prevent any pair from having a non-trivial common divisor strictly smaller than their minimum, we can map each number to a prime number or ensure they satisfy prime-based separation.
- Using a precomputed sieve (`is_prime`) and a `next_prime` lookup table, we can quickly find the smallest prime greater than or equal to each element `val` in `a`.
- Replacing elements with their corresponding valid prime values eliminates composite intersections that create disgusting gcd relationships, satisfying all constraints efficiently.

Logic:
1. Precompute primes up to `MAX_VAL = 200005` using a sieve, and build a `next_prime` lookup table from right to left.
2. Read the number of test cases `t`[cite: 14].
3. For each test case, read `n` and array `a`[cite: 14].
4. For each element, if it is prime, keep it; otherwise, replace it with the next available prime using the precomputed `next_prime` array.
5. Print the resulting transformed array elements separated by spaces[cite: 14].

Complexity Analysis:
- Time: O(MAX_VAL log log MAX_VAL) for precomputing primes, and O(N) per test case for array transformation.
- Space: O(MAX_VAL) to store the prime sieve and lookup arrays, plus O(N) for test case outputs.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

MAX_VAL = 200005
is_prime = [True] * MAX_VAL
is_prime[0] = is_prime[1] = False
for p in range(2, int(MAX_VAL**0.5) + 1):
    if is_prime[p]:
        for i in range(p * p, MAX_VAL, p):
            is_prime[i] = False

next_prime = [0] * MAX_VAL
last_p = MAX_VAL - 1
for i in range(MAX_VAL - 1, -1, -1):
    if is_prime[i]:
        last_p = i
    next_prime[i] = last_p

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        res = []
        for val in a:
            if is_prime[val]:
                res.append(val)
            else:
                p = next_prime[val]
                res.append(p)
                
        print(*res)

if __name__ == "__main__":
    solve()