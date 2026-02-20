"""
Day 20: Expression (Codeforces 479A)
Problem Link: https://codeforces.com/contest/479/problem/A

Logic:
Given three integers a, b, and c, we need to place '+' and '*' signs and 
parentheses to get the maximum possible value.
Since there are only two operators to place, the total combinations are few:
1. a + b + c
2. a * b * c
3. (a + b) * c
4. a * (b + c)
5. a + b * c
6. a * b + c

Complexity Analysis:
- Time: O(1) - Constant number of operations.
- Space: O(1).
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read the three integers
    try:
        a = int(input())
        b = int(input())
        c = int(input())
    except EOFError:
        return

    # Brute force all possible mathematical combinations
    ans1 = a + b + c
    ans2 = a * b * c
    ans3 = (a + b) * c
    ans4 = a * (b + c)
    ans5 = a + b * c
    ans6 = a * b + c

    # The result is the maximum of all these possibilities
    print(max(ans1, ans2, ans3, ans4, ans5, ans6))

if __name__ == "__main__":
    solve()