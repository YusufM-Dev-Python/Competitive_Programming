"""
Day 100: Milestone Reached! (2244B)
Topic: Implementation / Greedy
Logic:
1. Verify if the prefix sum of the array is sufficient at every point i.
2. The condition `curr_sum >= (i+1)*(i+2)//2` checks if the accumulated value 
   meets or exceeds the threshold required by the problem's growth constraint.
3. If this holds for all indices, the sequence is valid ("YES").

Complexity Analysis:
- Time: O(N) - Single pass through the array.
- Space: O(1) - Constant space used for tracking the current sum.
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

        curr_sum = 0
        yes = True

        for i in range(n):
            curr_sum += arr[i]
            # Check if current prefix sum meets the triangular threshold
            if curr_sum >= (i + 1) * (i + 2) // 2:
                continue
            else:
                yes = False
                break

        print("YES" if yes else "NO")

if __name__ == '__main__':
    solve()