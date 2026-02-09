# Day 10: Comparison String (Codeforces 1837B)
# Folder: Implementation
# Logic: Longest Monotonic Run. To satisfy a sequence of 'n' identical 
# comparison signs (e.g., '<<<<'), we need at least n+1 distinct numbers. 
# We find the longest such streak in the string.
# Time Complexity: O(n) - Single pass through the string.
# Space Complexity: O(1) - Only using counters.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input())
        s = input()

        curr_st = 1
        max_st = 1

        # Scanning for the longest streak of identical signs
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr_st += 1
            else:
                curr_st = 1
            
            if curr_st > max_st:
                max_st = curr_st
        
        # Minimum distinct numbers needed is streak length + 1
        print(max_st + 1)

if __name__ == "__main__":
    solve()