"""
Day 103: 2247A - Parity and Modular Constraints
Topic: Math / Implementation
Goal: Determine if the array can satisfy the condition based on its length 
      and total sum.

Logic:
1. Parity Check: If the length 'n' is odd, the problem constraints often make 
   a solution impossible ("NO").
2. Sum Condition: 
   - If the total sum is 0, it is trivially satisfied ("YES").
   - For non-zero sums, the problem requires the sum to be divisible by 4. 
     This often arises in problems where elements can be shifted or negated 
     in blocks of 4 to reach a target sum.
3. If these conditions are met, the array can be balanced.

Complexity Analysis:
- Time: O(N) per test case - One pass to calculate the sum.
- Space: O(N) to store the array, O(1) extra space.
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

        # If length is odd, a balanced state cannot be reached
        if n % 2 != 0:
            print("NO")
        else:
            total_sum = sum(arr)
            # A sum of 0 is always balanced. 
            # Otherwise, the sum must be divisible by 4 for the specific 
            # transformation rules in this problem.
            if total_sum == 0 or abs(total_sum) % 4 == 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()