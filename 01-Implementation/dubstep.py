"""
Day 31: Dubstep (Codeforces 208A)
Problem Link: https://codeforces.com/contest/208/problem/A

Logic:
1. The original song words are separated by one or more 'WUB' strings.
2. We replace all occurrences of 'WUB' with a space.
3. We use split() to extract the actual words (this ignores extra spaces).
4. We join the words back together with a single space.

Complexity Analysis:
- Time: O(N) - String replacement and splitting both take linear time.
- Space: O(N) - To store the resulting words.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    s = input()
    if not s: return
    
    # Replace WUB with space, split into list, join with single space
    result = " ".join(s.replace("WUB", " ").split())
    print(result)

if __name__ == "__main__":
    solve()