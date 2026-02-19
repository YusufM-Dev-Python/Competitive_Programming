"""
Day 19: Chat Room (Codeforces 58A)
Problem Link: https://codeforces.com/contest/58/problem/A

Logic:
We need to determine if "hello" is a subsequence of the input string 's'.
- We maintain a 'target' string: "hello".
- We use a pointer 'p2' to track how many characters of "hello" we've matched.
- We iterate through 's' once. If the current character matches target[p2],
  we move to the next character in the target.
- If the pointer reaches 5 by the end, we found the word.

Complexity Analysis:
- Time: O(N) where N is the length of the input string.
- Space: O(1) beyond input storage.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s = input()
    target = "hello"

    # Pointer for the target string "hello"
    p2 = 0

    for char in s:
        # Check if we still have characters in "hello" to find
        if p2 < 5:
            if char == target[p2]:
                # Found the next letter in the sequence!
                p2 += 1
        else:
            # We already found "hello", we can stop early
            break
        
    # If the pointer moved past the last index (4), we matched all 5 letters
    if p2 == 5:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()