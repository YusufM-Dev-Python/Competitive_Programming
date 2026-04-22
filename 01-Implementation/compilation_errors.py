"""
Day 64: A and B and Compilation Errors (Codeforces 519B)
Logic:
1. List 1: Initial errors.
2. List 2: Errors after first fix (1 missing).
3. List 3: Errors after second fix (1 missing from List 2).
4. Missing error 1 = Sum(List 1) - Sum(List 2)
5. Missing error 2 = Sum(List 2) - Sum(List 3)

Complexity Analysis:
- Time: O(N) - Linear pass for each summation.
- Space: O(N) - Storing the lists.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    line = input()
    if not line: return
    n = int(line)
    
    # Read the three lists of errors
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # Calculate sums
    sum_a = sum(a)
    sum_b = sum(b)
    sum_c = sum(c)
    
    # First missing error
    print(sum_a - sum_b)
    # Second missing error
    print(sum_b - sum_c)

if __name__ == "__main__":
    solve()