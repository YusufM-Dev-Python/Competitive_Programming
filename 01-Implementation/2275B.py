"""
Day 152: Codeforces 2275B - Stack / String Matching
Topic: Stack / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each test case, read string length `n` and the string `s`.
3. Use a stack to track indices of character '1' encountered in the string (1-indexed).
4. When encountering character '2', if the stack is not empty, pop the matching '1' index and record both or handle the pair.
5. Collect remaining unmatched indices, sort them, and print the count followed by the indices.

Complexity Analysis:
- Time: O(N \log N) per test case - due to sorting the final missing indices array.
- Space: O(N) - to store stack and missing indices.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        stack = []
        missing = []

        for i in range(len(s)):
            char = s[i]
            idx = i + 1

            if char == '1':
                stack.append(idx)
            elif char == '2':
                if stack:
                    stack.pop()
                    missing.append(idx)
        if stack:
            for ch in stack:
                missing.append(ch)

        missing.sort()
        print(len(missing))
        print(*missing)

if __name__ == "__main__":
    solve()