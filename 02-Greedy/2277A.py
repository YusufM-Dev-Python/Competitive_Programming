"""
Day 162: Codeforces 2277A - Subset Selecting[cite: 4]
Topic: Greedy / Counting / MEX Optimization
Question Extraction:
- We are given an array `a` of `n` integers and a positive integer `k`[cite: 4].
- We want to split elements into groups S_1, S_2, ..., S_m such that each group contains at least `k` elements, and each element belongs to at most one group[cite: 4].
- We want to maximize mex({max(S_1), max(S_2), ..., max(S_m)}), where mex(c) is the smallest non-negative integer not present in the collection[cite: 4].

Why we did this (Approach & Intuition):
- To achieve a MEX value of `ans`, we need to be able to form valid groups whose maximums cover all integers from `0` up to `ans - 1`.
- Specifically, to form a group with a maximum value of `i`, we need at least `k` elements in our array that are <= `i`. 
- By counting the frequencies of each element and maintaining a cumulative prefix sum of available elements up to each value `i`, we can greedily check how many contiguous MEX integers we can successfully unlock. If the cumulative count of elements <= `i` is at least `(i + 1) * k`, we can form valid groups for all values up to `i`, allowing us to push our MEX further.

Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and `k`, followed by the array `a`[cite: 4].
3. Compute the frequency count of each element in a frequency array up to size `n + 1`.
4. Iterate through potential MEX thresholds `i`, accumulating the `prefix_sum` of frequencies.
5. Check if the available elements can satisfy the group size requirement `(i + 1) * k`. If yes, update `ans = i + 1`; otherwise, break out and print the maximum achievable MEX.

Complexity Analysis:
- Time: O(N) per test case - linear pass to count frequencies and iterate through possible MEX values.
- Space: O(N) - to store the frequency array and input list.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        count = [0] * (n + 1)

        for x in a:
            count[x] += 1

        ans = 0
        prefix_sum = 0
        for i in range(n):
            if count[i] == 0:
                break
            prefix_sum += count[i]
            if prefix_sum >= (i + 1) * k:
                ans = i + 1
            else:
                break

        print(ans)
        
if __name__ == "__main__":
    solve()