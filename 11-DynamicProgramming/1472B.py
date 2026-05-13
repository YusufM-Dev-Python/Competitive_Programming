"""
Day 75: Long Jumps (Codeforces 1472B)
Topic: Dynamic Programming
Logic:
1. We want to find the maximum score starting from any index i.
2. The score at index i is: a[i] + (score at i + a[i], if that index exists).
3. By iterating backward from (n-1) down to 0, we can calculate the maximum 
   possible score for each starting point in O(1) time using previously 
   computed values.
4. This is a linear DP approach where score[i] represents the total path sum 
   starting from i.

Complexity Analysis:
- Time: O(N) - We perform a single pass through the array per test case.
- Space: O(N) - To store the DP 'score' array.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        # score[i] will store the maximum score if we start jumping from index i
        score = arr[:]

        # Process from right to left to build upon future jump results
        for i in range(n - 1, -1, -1):
            jump = i + arr[i]
            if jump < n:
                score[i] = arr[i] + score[jump]
            else:
                # If the jump goes out of bounds, the score is just the current element
                score[i] = arr[i]
        
        print(max(score))

if __name__ == "__main__":
    solve()