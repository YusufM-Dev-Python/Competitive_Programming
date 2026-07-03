"""
Day 91: String Mismatch / Love Story (Codeforces 1829A)
Topic: Strings / Implementation
Logic:
1. We are given a string 's' of length 10. We need to find how many characters differ 
   from the string "codeforces".
2. We compare characters at each corresponding index between 's' and our target template "codeforces".
3. For every mismatch found, we increment our counter.

Complexity Analysis:
- Time: O(1) per test case - Since the length of the string is fixed at 10, the loop runs exactly 10 times.
- Space: O(1) - Uses a static 10-character string reference.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    strt = "codeforces"
    t = int(input())
    for _ in range(t):
        count = 0
        s = input()
        
        # Compare each character position with the string "codeforces"
        for i in range(len(s)):
            if s[i] != strt[i]:
                count += 1
        print(count)
        
if __name__ == "__main__":
    solve()