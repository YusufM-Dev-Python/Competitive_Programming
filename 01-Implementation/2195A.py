"""
Day 148: Codeforces 2195A - Implementation / Search
Topic: Implementation / Basic Searching
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements `arr`.
3. Set a target value (`tar = 67`) and check if it exists within the array.
4. Print "YES" if found, otherwise print "NO".

Complexity Analysis:
- Time: O(N) per test case - linear scan to check membership in the list.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        tar = 67
        if tar in arr:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()