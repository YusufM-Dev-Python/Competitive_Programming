# Day 12: Cover in Water (Codeforces 1900A)
# Folder: Implementation
# Logic: Pattern Recognition. Three dots '...' allow us to generate infinite 
# water using the second operation. If '...' exists, we only need 2 units.
# Otherwise, we need 1 unit for every '.' present.
# Time Complexity: O(n) - Substring check and count are linear.
# Space Complexity: O(n) - To store the input string.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # t: Number of test cases
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        n = int(input()) # Number of cells
        s = input()      # The grid string

        # The "Infinite Water" Shortcut:
        # If we find 3 empty cells in a row, we only need 2 operations.
        if "..." in s:
            print(2)
        else:
            # Otherwise, we have to fill every single dot manually.
            print(s.count('.'))

if __name__ == "__main__":
    solve()