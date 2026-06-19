"""
Day 82 (Bonus): ICPC Balloons (Codeforces 1703B)
Topic: Implementation / Strings
Logic:
1. Every time a problem is solved, the team gets 1 balloon. This accounts for len(s) balloons.
2. The first team to solve a problem gets an additional bonus balloon. This means every 
   unique problem solved gets 1 extra balloon, which accounts for len(set(s)) balloons.
3. Therefore, total balloons = len(s) + len(set(s)).

Complexity Analysis:
- Time: O(N) per test case - Constructing the set takes linear time relative to string length.
- Space: O(N) - Storing unique characters in the set (bounded by O(26) for uppercase English letters).
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        uniq = set(s)
        print(len(uniq) + len(s))

if __name__ == "__main__":
    solve()