"""
Day 101: 2230B - Cost Optimization
Topic: Greedy / Math
Goal: Minimize the total cost to buy exactly 'n' items where items can be bought 
      individually for cost 'a' or in a bundle of 3 for cost 'b'.

Logic:
There are three primary strategies to reach 'n' items:
1. 'exact': Buy as many bundles of 3 as possible, then buy the remainder (0, 1, or 2) 
   individually. 
   Formula: (n // 3) * b + (n % 3) * a
   
2. 'b_too_much': Buy everything individually at cost 'a'. This is useful if the 
   bundle price 'b' is more expensive than buying 3 items individually.
   Formula: n * a
   
3. 'a_too_exp': Buy only bundles of 3, even if it means buying more than 'n' 
   items (rounding up to the nearest multiple of 3). This is useful if 'b' is 
   extremely cheap.
   Formula: ((n + 2) // 3) * b 
   Note: (n + 2) // 3 is a clean way to perform ceiling division: ceil(n / 3).

Complexity Analysis:
- Time: O(1) - Constant time arithmetic operations per test case.
- Space: O(1) - No extra structures needed.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n, a, b = map(int, input().split())

        # Strategy 1: Use bundles for the bulk, individuals for the remainder
        exact = (n // 3) * b + (n % 3) * a
        
        # Strategy 2: Buy only individuals (ignores bundles)
        b_too_much = n * a
        
        # Strategy 3: Buy only bundles (covers n, might exceed n)
        # We use (n + 2) // 3 to get ceiling(n / 3)
        a_too_exp = ((n + 2) // 3) * b

        # The answer is the cheapest of these three strategies
        print(min(exact, b_too_much, a_too_exp))

if __name__ == "__main__":
    solve()