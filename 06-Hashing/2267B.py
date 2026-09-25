"""
Day 140: Codeforces 2267B - Frequency Mapping / Sorting
Topic: Hash Maps / Sorting / Implementation
Logic:
1. Read the number of test cases `t`.
2. For each testcase, read `n` and the array elements.
3. Compute the frequency of each element using a dictionary.
4. Extract unique values in descending order and determine the maximum frequency.
5. Iterate through frequency levels from 1 up to the `max_freq`, appending available unique values at each level to construct the resulting arranged sequence, and print it.

Complexity Analysis:
- Time: O(N log N) per testcase - due to sorting the unique values by frequency/value.
- Space: O(N) - to store the frequency dictionary and the array elements.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        freq = {}
        for val in arr:
            freq[val] = freq.get(val, 0) + 1

        vals_desc = sorted(freq.keys(), reverse=True)
        max_freq = max(freq.values())

        ans = []
        for level in range(1, max_freq + 1):
            for v in vals_desc:
                if freq[v] >= level:
                    ans.append(v)

        print(*ans)

if __name__ == "__main__":
    solve()