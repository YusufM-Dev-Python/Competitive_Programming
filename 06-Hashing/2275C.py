"""
Day 153: Codeforces 2275C - Frequency Mapping with Anti-Hash-Bombing Protection
Topic: Hash Maps / Randomized Hashing / Parity Tracking
Logic:
1. Initialize a random 32-bit integer `R` to randomize dictionary keys via XOR hashing, mitigating worst-case hash collisions (anti-hash tests).
2. For each test case, compute triplet values with the random mask applied: `vals[i] = (arr[i] + arr[i+2] - arr[i+4]) ^ R`.
3. Use `defaultdict` along with parity tracking (`all_odd`, `all_even`, `valid_odd`, `valid_even`) and a sliding window distance constraint (`add_idx = i - 6`) to accumulate valid pairs.
4. Print the total matched count securely without fear of TLE due to hash collisions.

Complexity Analysis:
- Time: O(N) per test case - optimal linear pass with randomized hash map operations.
- Space: O(N) - to store frequency dictionaries and arrays.
"""

import sys
import random
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

R = random.getrandbits(32)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        vals = [(arr[i] + arr[i + 2] - arr[i + 4]) ^ R for i in range(n - 4)]

        all_odd = defaultdict(int)
        all_even = defaultdict(int)

        valid_odd = defaultdict(int)
        valid_even = defaultdict(int)

        ans = 0

        for i in range(n - 4):
            val = vals[i]
            p = i % 2

            add_idx = i - 6
            if add_idx >= 0:
                add_val = vals[add_idx]
                if add_idx % 2 == 0:
                    valid_even[add_val] += 1
                else:
                    valid_odd[add_val] += 1

            if p == 0:
                ans += all_odd[val]
                all_even[val] += 1
                ans += valid_even[val]
            else:
                ans += all_even[val]
                all_odd[val] += 1
                ans += valid_odd[val]

        print(ans)

if __name__ == "__main__":
    solve()