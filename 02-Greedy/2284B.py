"""
Day 168: Codeforces 2284B - Donation Ordering & Pleasant Count
Topic: Greedy / Sorting / Constructive
Question Extraction:
- We are given `n` donations and a target number `k` of very pleasant donations.
- A donation is very pleasant if its size is at least the average of all previous donations (a_m * (m - 1) >= sum from i=1 to m-1 of a_i), and the first donation is always very pleasant.
- We need to find an ordering of the donations such that exactly `k` donations are very pleasant, or output "NO" if no such arrangement exists.

Why we did this (Approach & Intuition):
- Sorting the donations allows us to strategically group and position elements to control when the running average threshold is met.
- The maximum element in the array has high leverage; if the required pleasant count `k` is less than the frequency of the maximum element (`c`), it is impossible to satisfy, so we output "NO".
- Otherwise, we can position smaller and medium elements carefully around the maximum elements using slicing and reversal, guaranteeing that exactly `k` donations qualify as very pleasant.

Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n`, `k`, and the list of donation values `a`.
3. Sort the array `a` and identify the maximum element `max_a` along with its frequency `c`.
4. Check if `k < c`; if so, print "NO".
5. Compute the remaining needed elements `j = k - c`, slice the middle elements into `first` and `last` parts, insert the maximum elements in between, and print "YES" followed by the arranged array.

Complexity Analysis:
- Time: O(N log N) per test case due to sorting the donation array.
- Space: O(N) to store the elements and output arrays.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        a.sort()

        max_a = a[-1]
        c = a.count(max_a)

        if k < c:
            print("NO")
            continue

        j = k - c
        mid = a[:n - c]
        cut = len(mid) - j

        first = mid[:cut]
        last = mid[cut:][::-1]
        ans = first + [max_a] * c + last

        print("YES")
        print(*ans)

if __name__ == "__main__":
    solve()