"""
Day 164: Codeforces 2259B - Minus Two[cite: 7]
Topic: Greedy / Parity Analysis / Number Theory Transformation
Question Extraction:
- We are given an array a_1, a_2, ..., a_n and can repeatedly apply the operation a_i = |a_i - 2| to all elements simultaneously[cite: 7].
- We want to find the maximum possible frequency of *any* single integer in the array after performing this operation an arbitrary number of times[cite: 7].

Why we did this (Approach & Intuition):
- Applying the operation x -> |x - 2| repeatedly affects numbers based on their parity and magnitude relative to 2. 
- Odd numbers remain odd and bounce back and forth under subtraction and absolute value.
- Even numbers can be categorized by dividing by 2 successively, grouping them by their divisor attributes (e.g., k = x // 2 and its parity).
- By counting elements falling into these distinct transformation trajectories (odds, even-k-even, even-k-odd), the maximum frequency we can ever concentrate onto a single target value is given by the largest group among these categories.

Logic:
1. Read the number of test cases `t`[cite: 7].
2. For each test case, read `n` and the array elements `arr`[cite: 7].
3. Categorize each element:
   - If it's odd, increment `odd_count`.
   - If it's even, compute `k = x // 2` and increment `even_k_even` if `k` is even, otherwise `even_k_odd`.
4. Take the maximum count among these categories (`odd_count`, `even_k_even`, `even_k_odd`) as the optimal frequency.
5. Print the resulting maximum frequency.

Complexity Analysis:
- Time: O(N) per test case - single linear pass through the array.
- Space: O(N) - to store the input array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        odd_count = 0
        even_k_even = 0
        even_k_odd = 0

        for x in arr:
            if x % 2 != 0:
                odd_count += 1
            else:
                k = x // 2
                if k % 2 == 0:
                    even_k_even += 1
                else:
                    even_k_odd += 1

        ans = max(odd_count, max(even_k_even, even_k_odd))
        print(ans)

if __name__ == "__main__":
    solve()