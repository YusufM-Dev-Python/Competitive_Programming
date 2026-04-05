"""
Day 48: Maximum Alternating Parity Subarray (Kadane's Variation)
Problem Link: https://codeforces.com/contest/1881/problem/C

Logic:
1. Standard Kadane's Algorithm finds the max subarray sum.
2. The twist: Subarray must have alternating parity (Odd, Even, Odd...).
3. If two adjacent elements have the same parity, the current subarray must end.
4. If the current sum becomes negative, it's better to start fresh.
5. Update max_sum at every step.

Complexity Analysis:
- Time: O(N) per test case.
- Space: O(N) to store the array.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        # Initialize with the first element
        curr_sum = arr[0]
        max_sum = arr[0]

        for i in range(1, n):
            # Reset Condition 1: Previous sum was dragging us down
            if curr_sum < 0:
                curr_sum = 0
            
            # Reset Condition 2: Parity constraint violated (Same parity)
            if arr[i-1] % 2 == arr[i] % 2:
                curr_sum = 0
            
            # Build the sum
            curr_sum += arr[i]
            
            # Track the global maximum
            if curr_sum > max_sum:
                max_sum = curr_sum

        print(max_sum)

if __name__ == "__main__":
    solve()