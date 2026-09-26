"""
Day 141: Codeforces 2267B - Simulation / Number Theory
Topic: Simulation / Implementation / Hashing
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array `arr`.
3. Define a helper function `sum_of_squares(x)` to compute the sum of the squares of digits of `x`.
4. For each element in the array, simulate the sequence of digit square sums for a fixed number of steps (`100` steps).
5. Extract the steady-state portion of the sequence (`tail_len` starting from index `30`), and count how many pairs share an identical tail sequence. Print the total count.

Complexity Analysis:
- Time: O(N * steps) per test case - tracking sequences for each element in the array.
- Space: O(N * steps) - to store the generated sequences.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def sum_of_squares(x):
    return sum(int(d) ** 2 for d in str(x))

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        steps = 100
        seqs = []

        for val in arr:
            curr = val
            seq = [curr]
            for _ in range(steps):
                curr = sum_of_squares(curr)
                seq.append(curr)
            seqs.append(seq)

        tail_len = 30
        ans = 0

        for i in range(n):
            tail_i = seqs[i][tail_len:]
            for j in range(i + 1, n):
                if tail_i == seqs[j][tail_len:]:
                    ans += 1
        print(ans)


if __name__ == "__main__":
    solve()