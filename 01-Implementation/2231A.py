"""
Day 163: Codeforces 2231A - Construct an Array[cite: 6]
Topic: Constructive / Implementation / Observations
Question Extraction:
- We are given an integer `n`[cite: 6].
- We need to construct an array of integers a_1, a_2, ..., a_n such that 1 <= a_i <= 2 * n for all i[cite: 6].
- All elements of the array and the sums of adjacent elements must be pairwise distinct (i.e., all {a_1, a_2, ..., a_n, a_1 + a_2, a_2 + a_3, ..., a_{n-1} + a_n} are unique)[cite: 6].

Why we did this (Approach & Intuition):
- By outputting odd numbers from 1 up to 2n - 1, we ensure that every single element in the array is unique and strictly odd.
- Furthermore, the sum of any two adjacent odd numbers is always an even number. Because all individual elements are odd and all adjacent sums are even, no individual element can ever equal any adjacent sum. This cleanly satisfies the distinctness condition without collisions.

Logic:
1. Read the number of test cases `t`[cite: 6].
2. For each test case, read integer `n`[cite: 6].
3. Construct the array by appending odd numbers ranging from 1 to 2 * n with a step of 2.
4. Print the resulting array elements separated by spaces.

Complexity Analysis:
- Time: O(N) per test case - linear construction of the array of size `n`.
- Space: O(N) - to store the generated array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(1, 2 * n + 1, 2):
            arr.append(i)

        print(*arr)

if __name__ == "__main__":
    solve()