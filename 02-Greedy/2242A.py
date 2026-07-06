"""
Day 94: Threshold Resource Check
Topic: Greedy / Implementation
Logic:
1. We need to satisfy a specific condition using an array of resource values.
2. The condition is met if:
   - We have at least one resource with a value >= 3.
   - OR we have at least two resources with a value >= 2.
3. We traverse the list once, incrementing counters for each threshold, and evaluate 
   the win condition at the end.

Complexity Analysis:
- Time: O(K) where K is the number of elements in the array.
- Space: O(1) - Using only two integer counters regardless of input size.
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        k = int(input())
        cards = list(map(int, input().split()))

        count_3 = 0
        count_2 = 0

        for val in cards:
            if val >= 3:
                count_3 += 1
            elif val >= 2:
                count_2 += 1
        
        # Check if the win condition is met
        if count_3 >= 1 or count_2 >= 2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()