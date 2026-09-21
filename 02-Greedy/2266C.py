"""
Day 139: Codeforces 2266C - String / Implementation
Topic: Greedy / Strings
Logic:
1. Read the number of test cases `t`.
2. For each test case, read length `n` and the binary string `s`.
3. Count the total number of zeros and ones in the string.
4. If the string starts with '1', output the total count of zeros.
5. If it starts with '0', iterate through the string maintaining prefix counts of zeros and ones to find the minimum operations required, then print the result.

Complexity Analysis:
- Time: O(N) per testcase - single pass to count and another pass to compute the minimum.
- Space: O(N) - to store the string `s`.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        
        zero = s.count('0')
        one = n - zero

        if s[0] == '1':
            print(zero)
        else:
            ans = n
            l_0 = 0
            l_1 = 0

            for i in range(n):
                if s[i] == '0':
                    l_0 += 1
                else:
                    l_1 += 1

                curr_ans = l_1 + (zero - l_0)
                ans = min(ans, curr_ans)

            print(ans)

if __name__ == '__main__':
    solve()