# Day 10: Prepend and Append (Codeforces 1791C)
# Folder: Implementation
# Logic: Two Pointers. We shrink the string from both ends as long as 
# s[st] and s[end] are different (one is '0', the other is '1'). 
# The remaining distance between pointers is the length of the original string.
# Time Complexity: O(n) - We traverse the string at most once.
# Space Complexity: O(1) - Only using two integer pointers.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # t: Number of test cases
    t_str = input()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        n = int(input()) # Length of the final string
        s = input()

        st = 0
        end = n - 1

        # While pointers haven't met and the ends are different ('0' and '1' or vice versa)
        while st < end:
            if s[st] != s[end]:
                st += 1
                end -= 1
            else:
                # If they are the same, we cannot 'un-prepend' or 'un-append'
                break
        
        # Calculate the length of the remaining middle part
        print(end - st + 1)

if __name__ == "__main__":
    solve()