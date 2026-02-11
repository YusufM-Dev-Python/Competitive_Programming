# Day 12: Extremely Round (Codeforces 1766A)
# Logic: Each digit place (10, 100, etc.) has exactly 9 extremely round numbers.
# We sum 9 for every full power of 10 and add the leading digit of the current number.
# Time Complexity: O(t) 
# Space Complexity: O(1)

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    for _ in range(t):
        s = input()
        print(9 * (len(s) - 1) + int(s[0]))

if __name__ == "__main__":
    solve()