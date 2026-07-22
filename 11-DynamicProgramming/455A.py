"""
Day 107: 455A - Boredom (Dynamic Programming)
Topic: Dynamic Programming
Goal: Maximize points by choosing numbers such that picking 'x' eliminates 'x-1' and 'x+1'.

Logic:
1. Frequency Counting: Count how many times each number appears in the array. 
   Since the maximum value is bounded (up to 100,000), we can use a frequency array.
2. State Transition: 
   - For each number 'i', we have two choices:
     a. Skip 'i': Our total points up to 'i' will be the same as up to 'i-1' (`dp[i-1]`).
     b. Take 'i': If we take all instances of 'i', we earn `i * count[i]` points, 
        but we cannot take 'i-1'. Thus, we add this to the best score up to 'i-2' (`dp[i-2]`).
3. Recurrence Relation: `dp[i] = max(dp[i-1], dp[i-2] + i * count[i])`

Complexity Analysis:
- Time: O(N + MAX_VAL) - Linear pass to count inputs, followed by a linear scan up to max value.
- Space: O(MAX_VAL) - To store the frequency and DP tables.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n_input = input()
    if not n_input: return
    n = int(n_input)
    arr = list(map(int, input().split()))

    MAX_VAL = 100005
    count = [0] * MAX_VAL

    # Step 1: Count frequencies of each element
    for num in arr:
        count[num] += 1

    # Step 2: Initialize DP table
    dp = [0] * MAX_VAL
    dp[1] = count[1] * 1

    # Step 3: Fill DP table using the max choice (skip vs. take)
    for i in range(2, MAX_VAL):
        left_sc = dp[i - 1]                  # Option 1: Skip current element i
        take_sc = dp[i - 2] + count[i] * i   # Option 2: Take all instances of element i

        dp[i] = max(left_sc, take_sc)
    
    # The answer will be the maximum value stored in our DP table
    print(max(dp))
        
if __name__ == '__main__':
    solve()