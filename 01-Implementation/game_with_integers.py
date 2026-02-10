# Day 11: Game with Integers (Codeforces 1899A)
# Folder: Implementation
# Logic: Game Theory. If n is not a multiple of 3, the First player 
# can add or subtract 1 to make it a multiple of 3 in the first move.
# If n is already a multiple of 3, the Second player can always 
# counteract the First player's move to prevent them from winning.
# Time Complexity: O(t) - Constant time check per test case.
# Space Complexity: O(1) - No extra memory.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # t: Number of test cases
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())

        # If n is not divisible by 3, First player makes it so in 1 move.
        if n % 3 != 0:
            print("First")
        else:
            # If n is already a multiple of 3, First player is forced 
            # to move to a non-multiple, and Second player can block.
            print("Second")

if __name__ == "__main__":
    solve()