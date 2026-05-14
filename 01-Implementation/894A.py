"""
Day 76: QAQ (Codeforces 894A)
Topic: Brute Force / Strings
Logic:
1. The goal is to count how many times the subsequence "QAQ" appears in a given string.
2. We use three nested loops with indices i, j, and k such that i < j < k.
3. If s[i] == 'Q', s[j] == 'A', and s[k] == 'Q', we increment our counter.
4. Note: While O(N^3) works for N=100, an O(N) approach is possible by counting 
   'Q's to the left and right of every 'A'.

Complexity Analysis:
- Time: O(N^3) - Triple nested loop over the string length.
- Space: O(1) - Only using a counter variable.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    s = input()
    ans = 0

    # Brute force check for all triplets (i, j, k) where i < j < k
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q':
                    ans += 1
    print(ans)
        
if __name__ == "__main__":
    solve()