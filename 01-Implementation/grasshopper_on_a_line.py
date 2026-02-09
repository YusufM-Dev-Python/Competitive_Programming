# Day 10: Grasshopper on a Line (Codeforces 1829A)
# Folder: Implementation
# Logic: Constructive Algorithm. If target 'x' is not divisible by 'k', 
# we take 1 jump. If it is, we split 'x' into (x-1) and 1. 
# Since 'x' is divisible by 'k', (x-1) cannot be (unless k=1, which isn't the case).
# Time Complexity: O(n) - One check per test case.
# Space Complexity: O(1) - No extra storage used.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: Number of test cases
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        # x: destination, k: forbidden multiple
        x, k = map(int, input().split())

        # Case 1: The direct path is clear.
        if x % k != 0:
            print(1)
            print(x)

        # Case 2: The destination is blocked. 
        # We take a small side-step (x-1) and then a tiny hop (1).
        else:
            print(2)
            print(x - 1, 1)

if __name__ == "__main__":
    solve()