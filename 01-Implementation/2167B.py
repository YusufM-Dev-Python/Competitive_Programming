"""
Day 130: 2167B - String Permutation and Anagram Validation
Topic: Strings / Sorting
Goal: Determine whether string 's' can be transformed into or matched with 't' 
      by comparing their sorted character representations.

Logic:
1. Input Handling: Read query count and string pairs for each test case.
2. Sorting Comparison: Sort the characters of both strings `s` and `t`.
3. Decision: If their sorted character arrays match exactly, output "YES"; otherwise, output "NO".

Complexity Analysis:
- Time: $\mathcal{O}(N \log N)$ per query due to sorting strings of length $N$.
- Space: $\mathcal{O}(N)$ to store string characters and sorted results.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    q_input = input()
    if not q_input: return
    q = int(q_input)
    
    for _ in range(q):
        n = int(input())
        s, t = input().split()
        
        # Compare sorted character representations of both strings
        if sorted(s) == sorted(t):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()