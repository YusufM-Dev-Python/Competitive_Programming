"""
Day 80: Vasya and Petya's Game / Pair Enumeration
Topic: Brute Force / Implementation
Logic:
1. We need to find all valid pairs of scores (i, j) such that Vasya's score 'i' is strictly greater than Petya's score 'j'.
2. Vasya's score can range from 'a' to 'x' inclusive.
3. Petya's score can range from 'b' to 'y' inclusive.
4. We execute a nested loop to check every possible pair. If i > j, we record the pair and increment our score tracker.

Complexity Analysis:
- Time: O(X * Y) - Due to the nested loops checking all score combinations.
- Space: O(X * Y) - To store the valid coordinate pairs in a list for printing.
"""

import sys

input = lambda:sys.stdin.readline().rstrip()

def solve():
    x, y, a, b = map(int, input().split())
    v_score = 0
    box = []
    
    # Iterate through all possible scores for Vasya and Petya
    for i in range(a, x + 1):
        for j in range(b, y + 1):
            if i > j:
                v_score += 1
                box.append((i, j))

    print(v_score)
    for i, j in box:
        print(f"{i} {j}") 

if __name__ == "__main__":
    solve()