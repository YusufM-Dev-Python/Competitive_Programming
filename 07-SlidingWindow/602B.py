"""
Day 107 (Part 2): 602B - Approximating a Constant Range
Topic: Two Pointers / Sliding Window / Hash Map
Goal: Find the length of the longest contiguous subsegment where the difference 
      between the maximum and minimum elements is at most 1.

Logic:
1. Sliding Window & Map: Maintain a sliding window using pointers `l` and `r`. 
   Use a hash map (`mappi`) to track the frequencies of elements currently inside the window.
2. Condition Management: 
   - Since the maximum minus the minimum in the range must be $\le 1$, and adjacent elements 
     differ by at most 1, this condition is equivalent to having **at most 2 unique values** 
     in our frequency map at any given time.
   - Expand the window by moving `r` forward and adding `arr[r]` to the map.
   - If the number of unique elements (`len(mappi)`) exceeds 2, shrink the window from the left 
     by incrementing `l` and updating/removing element frequencies until valid conditions are restored.
3. Track the maximum valid window length (`max_len`) encountered.

Complexity Analysis:
- Time: O(N) per test case - Each element enters and leaves the sliding window at most once.
- Space: O(N) in the worst case for the frequency map storing unique elements.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    l = 0
    max_len = 0
    mappi = {}

    # Sliding window traversal
    for r in range(n):
        # Add current element to the frequency map
        mappi[arr[r]] = mappi.get(arr[r], 0) + 1

        # If there are more than 2 unique values, the range condition (max - min <= 1) is violated
        while len(mappi) > 2:
            mappi[arr[l]] -= 1
            if mappi[arr[l]] == 0:
                del mappi[arr[l]]
            l += 1
        
        # Update the maximum length of the valid subsegment found
        max_len = max(max_len, r - l + 1)
    
    print(max_len)

if __name__ == "__main__":
    solve()