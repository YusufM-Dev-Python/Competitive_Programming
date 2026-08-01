"""
Day 116: 2248A - Contest Problem String Manipulation
Topic: Implementation / Strings
Goal: Process test case strings by removing specific target elements 
      and formatting the remainder.

Logic:
1. Input Handling: Read number of test cases and ingest each string as a mutable character list.
2. Character Removal: Safely remove target tokens (e.g., '1' and '0' based on contest rules).
3. Reconstruction: Join the remaining characters back into a string and print the result.

ComplexityAnalysis:
- Time: O(N) per test case - List removal operations scale with string length N.
- Space: O(N) to store the character list representation.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        s = list(input())

        # Contest specific character removal logic
        if '1' in s:
            s.remove('1')
        if '0' in s:
            s.remove('0')

        print("".join(s))
            

if __name__ == "__main__":
    solve()