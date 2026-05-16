"""
Day 78 (Bonus): New Year and Hurry (Codeforces 750A)
Topic: Greedy / Math / Implementation
Logic:
1. Limak has a total of 4 hours (240 minutes) available. 
2. The total time left to solve problems is (240 - k) minutes, where 'k' is the travel time.
3. The time required for the i-th problem is 5 * i minutes.
4. We can simulate the process by greedily accumulating the time taken for each problem 
   from 1 to n. If adding the time for the next problem keeps us within the remaining limit, 
   we increment our count. Otherwise, we stop.

Complexity Analysis:
- Time: O(N) - Linear loop iterating up to n problems. (Can also be solved in O(1) using math/binary search, but N <= 10 makes O(N) optimal).
- Space: O(N) - Storing problem times in an array (can be optimized to O(1) by removing the array).
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    n, k = map(int, input().split())

    # Total contest time is 4 hours = 240 minutes
    rem = 240 - k
    prob = []
    ans = 0
    
    # Precompute the time required for each problem
    for i in range(1, n + 1):
        prob.append(5 * i)
    
    curr = 0
    # Greedily solve problems as long as there is time left
    for i in range(n):
        curr += prob[i]
        if curr <= rem:
            ans += 1
        else:
            break
            
    print(ans)
            
if __name__ == "__main__":
    solve()