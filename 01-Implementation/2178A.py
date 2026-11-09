"""
Day 170: Codeforces 2178A - Character Counting
Topic: String / Counting / Implementation
Question Extraction:
- We are given a string `s`.
- We need to determine if it is valid based on a specific character frequency constraint, specifically checking the occurrence of the character 'Y'.

Why we did this (Approach & Intuition):
- The problem imposes a strict threshold on the maximum allowable occurrences of 'Y' to keep the string valid.
- By using the built-in string counting method, we can scan the string in a single pass to check if the count of 'Y' exceeds 1. If it does, the condition fails. 

Logic:
1. Read the number of test cases `t`.
2. For each test case, read the input string `s`.
3. Count the occurrences of the character "Y" in the string using `s.count("Y")`.
4. If the count is less than or equal to 1, print "YES".
5. Otherwise, print "NO".

Complexity Analysis:
- Time: O(N) per test case, where N is the length of the string, due to the linear scan by `.count()`.
- Space: O(1) beyond storing the input string.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        s = input()

        if s.count("Y") <= 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()