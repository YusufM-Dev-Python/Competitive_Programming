"""
Day 112 (Part 2): 1660C - Get an Even String
Topic: Strings / Greedy
Goal: Find the minimum number of characters to delete from a string so that 
      every adjacent pair of identical characters forms valid even segments.

Logic:
1. Greedy Pairing: Iterate through the string using a set (`ans`) to track unique 
   characters since the last completed pair.
2. If the current character is already in the set, it means we found a matching pair (e.g., "aa" or "bb"). 
   We increment our matched character count (`count += 2`) and clear the set to reset for the next pair.
3. If it's not in the set, we add it and continue.
4. The minimum deletions required will be the total length of the string minus the number 
   of characters that successfully formed valid pairs (`len(s) - count`).

Complexity Analysis:
- Time: O(N) per test case - Single linear pass through the string.
- Space: O(K) where K is the alphabet size stored in the set (at most 26 lowercase English letters).
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        s = input()

        ans = set()
        count = 0

        # Greedy pass to count how many characters can form valid pairs
        for char in s:
            if char not in ans:
                ans.add(char)
            else:
                count += 2
                ans.clear()  # Reset set for the next pair search

        # Total characters minus matched pairs gives minimum deletions needed
        print(len(s) - count)

if __name__ == "__main__":
    solve()