"""
Day 159: Codeforces 2261D1 - Interval Construction / Case Analysis
Topic: Constructive / Implementation / Greedy
Logic:
1. Read the number of test cases `t` and use an output buffer for fast batch printing.
2. Handle base cases explicitly:
   - For `n == 1`, output `0` intervals.
   - For `n == 2`, output `1` interval (`1 1`).
   - For `n == 3`, output `2` intervals (`1 1` and `3 3`).
3. For larger values of `n`, determine parity bounds (`p`), build the interval sequence step-by-step using tuples, and handle odd/even remainders accordingly.
4. Output the total count of constructed intervals followed by each interval pair.

Complexity Analysis:
- Time: O(N) per test case - linear construction of the interval sequence.
- Space: O(N) - to store output strings and sequences.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    out = []
    for _ in range(t):
        n, m = map(int, input().split())  # Note: m read alongside n based on input structure

        if n == 1:
            out.append("0")
        elif n == 2:
            out.append("1")
            out.append("1 1")
        elif n == 3:
            out.append("2")
            out.append("1 1")
            out.append("3 3")
        else:
            p = n if n % 2 == 0 else n - 1
            seq = [(1, 2)]
            x = 2
            while x <= p - 4:
                seq.append((x, x + 2))
                x += 2
            seq.append((p - 2, p - 1))
            if n % 2 == 1:
                seq.append((n, n))

            out.append(str(len(seq)))
            for l, r in seq:
                out.append(f"{l} {r}")

    print("\n".join(out))

if __name__ == "__main__":
    solve()