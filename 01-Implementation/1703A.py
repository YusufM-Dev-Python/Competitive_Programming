"""
Day 81 (Bonus): YES or YES? (Codeforces 1703A)
Topic: Implementation / Strings
Logic:
1. The problem asks us to determine if a given string of length 3 is a case-insensitive 
   match for the word "YES".
2. We convert the input string to lowercase using the .lower() method.
3. If the normalized string matches "yes", we output "YES". Otherwise, we output "NO".

Complexity Analysis:
- Time: O(1) per test case - The string length is fixed at 3.
- Space: O(1) - Temporary lower-case copy of a 3-character string.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        new_s = s.lower()

        # Check if the normalized string matches "yes"
        if new_s == "yes":
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()