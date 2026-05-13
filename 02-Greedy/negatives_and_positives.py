"""
Day 61 Sunday Finisher: Negatives and Positives (Codeforces 1791E)
Logic:
1. Flipping adjacent signs (a_i, a_{i+1}) allows moving negative signs freely.
2. If the total count of negatives is even, all can become positive.
3. If the count is odd, exactly one number must remain negative.
4. To maximize the sum, we choose the number with the smallest absolute 
   value to be the one that stays (or becomes) negative.

Complexity Analysis:
- Time: O(N) - We only need one pass to find the sum and the minimum absolute value.
- Space: O(N) - To store the array (O(1) if reading on the fly).
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

        neg_count = 0
        total_abs_sum = 0
        min_abs_val = float('inf')

        for x in arr:
            if x < 0:
                neg_count += 1
            
            abs_x = abs(x)
            total_abs_sum += abs_x
            if abs_x < min_abs_val:
                min_abs_val = abs_x

        # If we have an even number of negatives, all become positive
        if neg_count % 2 == 0:
            print(total_abs_sum)
        else:
            # If odd, we must subtract the smallest absolute value twice 
            # (once because it shouldn't have been added, once to make it negative)
            print(total_abs_sum - 2 * min_abs_val)

if __name__ == "__main__":
    solve()