# Day 10: Contest Problem 2194A
# Folder: Implementation
# Logic: Periodic Removal. We calculate how many full blocks of size 'w' 
# fit into 'n' and subtract that count from the total.
# Time Complexity: O(m) - Constant time calculation per test case.
# Space Complexity: O(1) - No extra data structures used.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # m: Number of test cases
    m_input = input()
    if not m_input: return
    m = int(m_input)

    for _ in range(m):
        # n: Total value, w: The divisor/period
        n, w = map(int, input().split())

        # The calculation: Total minus the count of full blocks
        print(n - (n // w))

if __name__ == "__main__":
    solve()