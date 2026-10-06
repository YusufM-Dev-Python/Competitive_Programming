"""
Day 151: Codeforces 2108B - Bit Manipulation / Parity Tricky Case
Topic: Bit Manipulation / Case Analysis
Logic:
1. Read the number of test cases `t`.
2. For each testcase, read `n` and `x`.
3. Handle the base case where `x == 0`: 
   - If `n == 1`, it's impossible, so output `-1`.
   - If `n` is even, output `n`.
   - If `n` is odd, output `n + 3` to satisfy the constraints.
4. When `x > 0`:
   - Count the number of set bits in `x` (`p = bin(x).count("1")`).
   - If `n <= p`, the required elements can be formed directly, so output `x`.
   - Handle remaining parity differences (`n - p`) using conditional adjustments based on whether the difference is even or odd, and special handling when `x == 1`.

Complexity Analysis:
- Time: O(\log X) per test case - counting set bits via binary string conversion.
- Space: O(1) - constant memory.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())

        if x == 0:
            if n == 1:
                ans = -1
            elif n % 2 == 0:
                ans = n
            else:
                ans = n + 3  
        else:
            p = bin(x).count("1")
            if n <= p:
                ans = x
            elif (n - p) % 2 == 0:
                ans = (n - p) + x
            elif x == 1:
                ans = n + 3
            else:
                ans = (n - p) + x + 1

        print(ans)

if __name__ == "__main__":
    solve()