"""
Day 103 (Part 2): 2247B - Constructive Partition
Topic: Constructive Algorithms
Goal: Construct an array of length 'n' where the sum is 'm' and at least 'k' 
      elements meet specific criteria.

Logic:
1. Feasibility: The total sum 'm' must be at least 'k' because each of the 
   required 'k' elements must be at least 1. If m < k, it is impossible ("NO").
2. Construction Strategy:
   - We need to ensure 'k' elements satisfy the condition. The easiest way to 
     satisfy this is to set the first k-1 elements to 1.
   - We assign the remainder of the total sum (m - (k - 1)) to the k-th element 
     (index k-1), ensuring the total sum remains exactly 'm'.
   - The remaining n-k elements are simply set to 1 (or any valid value) to 
     fill the array length to 'n'.
3. This construction guarantees the sum is 'm' and handles the constraints efficiently.

Complexity Analysis:
- Time: O(N) per test case - One pass to fill the array and print.
- Space: O(N) - To store the result array.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n, k, m = map(int, input().split())
        
        # Check if it is even possible to have k elements summing to m 
        # (since each element must be at least 1).
        if m < k:
            print("NO")
        else:
            print("YES")
            ans = [0] * n
            
            # Fill the first k-1 elements with 1
            for i in range(k - 1):
                ans[i] = 1
            
            # Assign the remaining required sum to the k-th element
            ans[k - 1] = m - (k - 1)
            
            # Fill any remaining spots with 1
            for i in range(k, n):
                ans[i] = 1
                
            print(*ans)

if __name__ == "__main__":
    solve()