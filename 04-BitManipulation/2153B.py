"""
Day 160: Codeforces 2153B - Bitwise Reversion[cite: 3]
Topic: Bit Manipulation / Conditional Logic
Question Extraction:
- We are given three non-negative integers x, y, and z[cite: 3].
- We need to determine if there exist integers a, b, and c such that:
  * a & b = x[cite: 3]
  * b & c = y[cite: 3]
  * a & c = z[cite: 3]
  
Why we did this (Approach & Intuition):
- By combining the bitwise AND equations, we see that:
  * x & y = (a & b) & (b & c) = a & b & c
  * y & z = (b & c) & (a & c) = a & b & c
  * x & z = (a & b) & (a & c) = a & b & c
- This means all three pairwise combinations must evaluate to the exact same shared value (a & b & c).
- Therefore, checking if (x & y) == (y & z) == (x & z) is both necessary and fully sufficient to guarantee the existence of valid a, b, and c.

Logic:
1. Read the number of test cases `t` and use an output list for fast batch printing.
2. For each test case, read the three target integers `x`, `y`, and `z`[cite: 3].
3. Check the derived mathematical identity: (x & y) == (y & z) == (x & z).
4. Append "YES" if the condition matches, otherwise "NO"[cite: 3].
5. Print all results joined by newlines.

Complexity Analysis:
- Time: O(1) per test case - constant time bitwise and equality evaluations.
- Space: O(T) - to store output results for fast batch printing.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    out = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        if (x & y) == (y & z) == (x & z):
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))


if __name__ == "__main__":
    solve()