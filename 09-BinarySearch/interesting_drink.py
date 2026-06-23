"""
Day 63: Interesting Drink (Codeforces 706B)
Logic:
1. Sort shop prices once to enable binary search.
2. For each query 'm' (daily budget), find the number of shops 
   with price <= m.
3. This is equivalent to finding the 'upper bound' index—the 
   first index where price > m.

Complexity Analysis:
- Time: O(N log N) for sorting + O(Q log N) for queries.
- Space: O(N) to store shop prices.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Read shop data
    try:
        line1 = input()
        if not line1: return
        n = int(line1)
        arr = list(map(int, input().split()))
        
        # Read query data
        q = int(input())
        
        # Sort prices to allow binary search
        arr.sort()
        
        results = []
        for _ in range(q):
            m = int(input())

            l = 0
            r = n - 1

            # Standard Binary Search for Upper Bound (bisect_right)
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= m:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # The 'l' pointer naturally ends up at the count of elements <= m
            results.append(str(l))
        
        # Output all results at once for speed
        sys.stdout.write('\n'.join(results) + '\n')
                
    except EOFError:
        pass

if __name__ == "__main__":
    solve()