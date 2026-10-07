"""
Day 152: Codeforces 2275C - Frequency Mapping / Parity Tracking
Topic: Hash Maps / Two Pointers / Counting
Logic:
1. Fast I/O is used to read inputs.
2. For each test case, compute the custom triplet expression values: `vals[i] = arr[i] + arr[i+2] - arr[i+4]` for valid indices up to `n - 4`.
3. Maintain frequency maps (`all_odd`, `all_even`) split by parity to track element counts across matching parities.
4. Use a sliding window approach with a distance constraint (`add_idx = i - 6`) to transition elements into valid status dictionaries (`valid_odd`, `valid_even`) once they satisfy spacing requirements.
5. Aggregate valid matching pairs according to parity conditions and accumulate the total count (`ans`).

Complexity Analysis:
- Time: O(N) per test case - single pass iteration with dictionary lookups.
- Space: O(N) - to store the frequency dictionaries and values array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        vals = [arr[i] + arr[i + 2] - arr[i + 4] for i in range(n - 4)]

        all_odd = {}
        all_even = {}

        valid_odd = {}
        valid_even = {}

        ans = 0

        for i in range(n - 4):
            val = vals[i]
            p = i % 2

            add_idx = i - 6
            if add_idx >= 0:
                add_val = vals[add_idx]
                if add_idx % 2 == 0:
                    valid_even[add_val] = valid_even.get(add_val, 0) + 1
                else:
                    valid_odd[add_val] = valid_odd.get(add_val, 0) + 1

            if p == 0:
                ans += all_odd.get(val, 0)
                all_even[val] = all_even.get(val, 0) + 1
            else:
                ans += all_even.get(val, 0)
                all_odd[val] = all_odd.get(val, 0) + 1

            if p == 0:
                ans += valid_even.get(val, 0)
            else:
                ans += valid_odd.get(val, 0)  

        print(ans)

if __name__ == "__main__":
    solve()