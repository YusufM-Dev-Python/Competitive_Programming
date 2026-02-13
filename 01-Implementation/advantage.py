"""
Day 14: Advantage (Codeforces 1760C)
Problem Link: https://codeforces.com/contest/1760/problem/C

Logic:
For each participant, we need to find the difference between their score and 
the maximum score of any OTHER participant.
1. Identify the maximum (max1) and the second maximum (max2) in the array.
2. Iterate through the original array:
   - If the current score is max1, the best 'other' score is max2.
   - For all other scores, the best 'other' score is max1.
3. This ensures we don't compare a person to themselves.

Complexity Analysis:
- Time: O(N log N) due to sorting to find max1 and max2. 
  (Could be O(N) if finding maxes manually).
- Space: O(N) to store the input and the result list.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        
        # We need the two largest values to determine the 'other' maximum
        sorted_s = sorted(s)
        max1 = sorted_s[-1] 
        max2 = sorted_s[-2] 
        
        ans = []
        for x in s:
            # If the current person is the absolute winner
            if x == max1:
                # Compare them to the second-best person
                ans.append(x - max2)
            else:
                # Compare everyone else to the absolute winner
                ans.append(x - max1)
                
        # Use asterisk to print the list elements separated by spaces
        print(*ans)

if __name__ == "__main__":
    solve()