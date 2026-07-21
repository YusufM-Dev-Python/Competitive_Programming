"""
Day 106 (Part 2): 1133C - Two Pointers / Sliding Window
Topic: Two Pointers / Sorting / Greedy
Goal: Find the maximum number of elements we can select such that the difference 
      between the maximum and minimum values in our selection is at most 5.

Logic:
1. Sorting: First, sort the array in ascending order. This guarantees that for 
   any window from index `l` to `r`, the minimum is at `arr[l]` and the maximum is at `arr[r]`.
2. Sliding Window:
   - Expand the right pointer `r` to include new elements.
   - If the difference `arr[r] - arr[l]` exceeds 5, increment the left pointer `l` 
     until the condition is restored.
   - At each step, update `max_ans` with the current window size `r - l + 1`.
3. This avoids an $O(N^2)$ brute-force check and solves the problem in optimal time.

Complexity Analysis:
- Time: O(N log N) due to the sorting step, followed by an O(N) linear pass with the two pointers.
- Space: O(N) to store the array elements.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    max_ans = 0
    # Step 1: Sort the array to enable sliding window logic
    arr.sort()

    l = 0

    # Step 2: Use two pointers (l and r) to maintain a valid window of difference <= 5
    for r in range(n):
        # Shrink the window from the left if the condition is violated
        while arr[r] - arr[l] > 5:
            l += 1
        
        # Track the maximum valid window size found so far
        max_ans = max(max_ans, r - l + 1)
    
    print(max_ans)

if __name__ == "__main__":
    solve()