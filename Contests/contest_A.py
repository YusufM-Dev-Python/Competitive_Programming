"""
Day 21: Contest Problem A
Logic:
The problem asks for the maximum 'score' (number of adjacent different characters)
given that we can cyclically rotate the string.
1. We simulate every possible rotation m from 0 to n-1.
2. For each rotation, we construct s[m:] + s[:m].
3. We count how many times rotated_s[i] != rotated_s[i+1].
4. The answer is the maximum count + 1 (since 0 transitions = 1 group).

Complexity Analysis:
- Time: O(N^2) - N rotations, each taking O(N) to check.
- Space: O(N) - To store the rotated string.
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
        s = input()

        # Base score is at least 1 (the string itself)
        max_score = 1
        
        # Try every possible cyclic shift
        for m in range(n):
            curr_score = 1
            # Construct the rotated string
            rotated_s = s[m:] + s[:m]

            # Count transitions between different characters
            for i in range(0, n - 1):
                if rotated_s[i] != rotated_s[i+1]:
                    curr_score += 1

            # Keep track of the best score found
            if curr_score > max_score:
                max_score = curr_score
                
        print(max_score)

if __name__ == "__main__":
    solve()