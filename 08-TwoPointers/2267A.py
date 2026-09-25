"""
Day 140: Codeforces 2267A - Two Pointers / Greedy
Topic: Two Pointers / Strings / Greedy
Logic:
1. Read the number of test cases `t`.
2. For each testcase, read the string length `n` and character `c`, followed by the string `s`.
3. Use a two-pointer approach starting from both ends (`l = 0`, `r = n - 1`) to move inward.
4. If characters at both pointers match, advance both pointers without any cost.
5. If they mismatch and one of them equals the target character `c`, increment the coin cost by 1. Otherwise, increment the coin cost by 2.
6. Print the total accumulated `coin` cost.

Complexity Analysis:
- Time: O(N) per testcase - traversing the string from both ends with two pointers.
- Space: O(N) - to store the input string `s`.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        line = input().split()
        n = line[0]
        c = line[1]

        s = input()

        l = 0
        r = int(n) - 1

        coin = 0

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r] and (s[l] == c or s[r] == c):
                coin += 1
                l += 1
                r -= 1
            else:
                coin += 2
                l += 1
                r -= 1

        print(coin)

if __name__ == "__main__":
    solve()