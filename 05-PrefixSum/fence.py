"""
Day 69: Fence (Codeforces 363B)
Logic:
1. We need to find a contiguous subsegment of length k with the minimum sum.
2. We use a prefix sum array to calculate any window sum in O(1).
3. Sum of window starting at index s (0-indexed) is: prefix[s+k] - prefix[s].
4. We track the minimum sum and the starting index (converting to 1-based).

Complexity Analysis:
- Time: O(N) - One pass to build prefix sums, one pass to find the min window.
- Space: O(N) - Storing the prefix sum array.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read n and k
    line1 = input().split()
    if not line1: return
    n, k = map(int, line1)
    
    # Read heights
    arr = list(map(int, input().split()))

    # Build Prefix Sum Array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    min_sum = float('inf')
    best_idx = 1 # Default to first plank

    # Slide the window of size k
    for s in range(n - k + 1):
        # Calculate sum of window [s, s+k-1]
        curr_sum = prefix[s+k] - prefix[s]

        if curr_sum < min_sum:
            min_sum = curr_sum
            best_idx = s + 1 # Convert to 1-based index
    
    print(best_idx)

if __name__ == "__main__":
    solve()