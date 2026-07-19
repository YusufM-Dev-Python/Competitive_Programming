"""
Day 104: 2247C - Array Transformation Logic
Topic: Implementation / Greedy
Goal: Transform array 'a' into 'b' using the minimum number of operations based 
      on element pairs.

Logic:
1. Classification:
   - p_10: Indices where a[i]=1 and b[i]=0 (these are your "transformable" units).
   - p_00: Indices where a[i]=0 and b[i]=0.
   - p_11: Indices where a[i]=1 and b[i]=1.
2. Strategy:
   - If arrays are already equal, 0 operations are needed.
   - If p_10 is odd, you can resolve the difference in 1 operation.
   - If p_10 is even and non-zero, you can resolve it in 2 operations.
   - If p_10 is 0, you need at least one (1, 1) pair and one (0, 0) pair to 
     bridge the transformation, requiring 2 operations. Otherwise, it's impossible (-1).

Complexity Analysis:
- Time: O(N) per test case - One pass to count pair types.
- Space: O(N) to store the arrays.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        p_10 = 0
        p_11 = 0
        p_00 = 0

        # Count the types of pairs at each index
        for i in range(n):
            if a[i] == 1 and b[i] == 0:
                p_10 += 1
            elif a[i] == 0 and b[i] == 0:
                p_00 += 1
            elif a[i] == 1 and b[i] == 1:
                p_11 += 1
        
        # Determine operations needed
        if a == b:
            print(0)
        elif p_10 % 2 != 0:
            print(1)
        elif p_10 % 2 == 0 and p_10 != 0:
            print(2)
        elif p_10 == 0:
            # If no (1, 0) pairs exist, check if we have enough context pairs
            if p_11 >= 1 and p_00 >= 1:
                print(2)
            else:
                print(-1) 

if __name__ == "__main__":
    solve()