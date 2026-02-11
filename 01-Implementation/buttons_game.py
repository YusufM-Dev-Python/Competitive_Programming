# Day 12: Buttons (Codeforces 1858A)
# Folder: Implementation
# Logic: Parity and Advantage. Both players will press the shared buttons (c) 
# until they are gone. If c is odd, Anna (First) gets one more button than Katie.
# We then simply compare the resulting 'effective' button counts.
# Time Complexity: O(t) - Simple comparison per test case.
# Space Complexity: O(1) - No extra storage.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)

    for _ in range(t):
        # a: Anna's buttons, b: Katie's buttons, c: Shared buttons
        a, b, c = map(int, input().split())
        
        # If the number of shared buttons is odd, 
        # Anna gets the last one, gaining a +1 advantage.
        if c % 2 != 0:
            a += 1
            
        # The player with more buttons wins. 
        # If equal, Second player (Katie) wins because Anna must move first.
        if a > b:
            print("First")
        else:
            print("Second")

if __name__ == "__main__":
    solve()