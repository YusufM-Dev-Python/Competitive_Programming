"""
Day 133: Array Frequency / Game Strategy
Topic: Implementation / Greedy
Logic:
1. We are given an array of elements consisting of 1s and 0s over multiple test cases.
2. We count the total occurrences of 1s (`c_1`) and 0s (`c_0`) in the given array.
3. If the count of 1s is greater than or equal to the count of 0s, Bessie wins, so we print "Bessie". Otherwise, Elsie wins and we print "Elsie".

Complexity Analysis:
- Time: O(N) per test case - Since we traverse the array to count the occurrences of 1s.
- Space: O(N) - To store the array elements in memory for each test case.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        c_1 = arr.count(1)
        c_0 = n - c_1

        if c_1 >= c_0:
            print("Bessie")
        else:
            print("Elsie")

if __name__ == "__main__":
    solve()