"""
Day 54: Water the Trees (Codeforces 1661C)
Logic:
1. Binary search for the minimum days 'mid' needed.
2. In 'mid' days:
   - pool_2 = mid // 2 (number of +2 waterings available)
   - pool_1 = mid - pool_2 (number of +1 waterings available)
3. Check Target (max_h) and Target (max_h + 1).
4. Requirement: 
   a) pool_1 must be >= the number of trees with odd differences.
   b) Total volume (pool_1 + pool_2 * 2) must be >= total height needed.

Complexity Analysis:
- Time: O(N * log(10^15)) - N elements per check, logarithmic search range.
- Space: O(N) - Storing the tree heights.
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
        h = list(map(int, input().split()))
        
        max_h = max(h)
        
        def get_best_day(anchor):
            odd_req = 0
            total_height_req = 0
            
            # Calculate mandatory +1s and total volume needed for this anchor
            for i in range(n):
                diff = anchor - h[i]
                total_height_req += diff
                if diff % 2 != 0:
                    odd_req += 1
            
            # Binary Search Check Function
            def check(D):
                pool_2 = D // 2
                pool_1 = D - pool_2
                # Must satisfy mandatory +1s AND total volume
                return pool_1 >= odd_req and (pool_1 + pool_2 * 2) >= total_height_req

            low = 0
            high = 10**15  # Large enough bound for any N and H
            best = high
            
            while low <= high:
                mid = (low + high) // 2
                if check(mid):
                    best = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return best

        # Check both the obvious target and the parity-shifted target
        ans1 = get_best_day(max_h)
        ans2 = get_best_day(max_h + 1)

        print(min(ans1, ans2))

if __name__ == "__main__":
    solve()