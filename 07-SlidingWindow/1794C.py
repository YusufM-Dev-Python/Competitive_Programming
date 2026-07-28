"""
Day 113 (Part 2): 1794C - Sliding Window Range Validation
Topic: Two Pointers / Sliding Window
Goal: For each ending position 'r', find the maximum length of a contiguous subarray 
      ending at 'r' such that every element satisfies the condition `arr[l] >= length`.

Logic:
1. Two Pointers / Sliding Window: We maintain a left pointer `l` and expand with `r`.
2. Condition Check: The core rule requires that the minimum element in the current window 
   (which, due to array properties or problem constraints, aligns efficiently with `arr[l]`) 
   must be at least equal to the window's length (`r - l + 1`).
3. If the condition is violated (`arr[l] < window_length`), we increment `l` until it holds true.
4. We record the valid window size `r - l + 1` for each position and output the resulting array.

Complexity Analysis:
- Time: O(N) per test case - Both pointers traverse the array linearly.
- Space: O(N) to store the result array of lengths.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        l = 0
        ans_len = [0] * n

        # Sliding window traversal to find the maximum valid subarray length ending at each index r
        for r in range(n):
            # Ensure the condition arr[l] >= window_length holds true
            while arr[l] < (r - l + 1):
                l += 1

            ans_len[r] = r - l + 1

        print(*ans_len)

if __name__ == "__main__":
    solve()