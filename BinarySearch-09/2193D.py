"""
Day 83: Dangerous Score Maximization
Topic: Binary Search / Prefix Sum / Greedy
Logic:
1. Sort array 'a' to enable efficient range queries via binary search.
2. Precompute a prefix sum array on 'b' to fetch the cumulative costs/weights 
   in O(1) time.
3. Iterate through every unique element 'diff' in array 'a':
   - First Binary Search: Find the first index 'valid_idx' where a[mid] >= diff. 
     This calculates how many elements ('valid_swords') satisfy the condition.
   - Second Binary Search: Determine the maximum number of levels ('level_done') 
     we can complete using the precomputed prefix sums without exceeding 'valid_swords'.
4. Track and maximize the total product score (diff * level_done).

Complexity Analysis:
- Time: O(N log N + U * log N) where N is array size and U is the number of unique elements in 'a'.
- Space: O(N) - Storing the prefix sums array.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a.sort()
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + b[i]

        max_score = 0
        for diff in set(a):
            l = 0
            r = n - 1
            valid_idx = n
            
            # First Binary Search: Find lower bound for the threshold 'diff'
            while l <= r:
                mid = (l + r) // 2
                if a[mid] >= diff:
                    valid_idx = mid
                    r = mid - 1 
                else:
                    l = mid + 1 
                    
            valid_swords = n - valid_idx

            l = 0
            r = n
            level_done = 0
            
            # Second Binary Search: Find maximum levels using prefix array
            while l <= r:
                mid = (l + r) // 2
                if prefix[mid] <= valid_swords:
                    level_done = mid
                    l = mid + 1
                else:
                    r = mid - 1  

            current_score = diff * level_done
            if current_score > max_score:
                max_score = current_score

        print(max_score)

if __name__ == "__main__":
    solve()