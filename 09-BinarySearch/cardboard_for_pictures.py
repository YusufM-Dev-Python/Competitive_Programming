"""
Day 60 (The Beast): Cardboard for Pictures (Codeforces 1850E)
Logic:
1. We have n square paintings with sides s_1, s_2, ..., s_n.
2. We add a uniform border of width 'w' to all of them.
3. Total area C = sum of (s_i + 2w)^2 for all i.
4. Since the area function is strictly increasing with w, we binary search for w.

Complexity Analysis:
- Time: O(N * log(10^9)) - For each binary search step, we iterate through n paintings.
- Space: O(N) - To store the painting sides.
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n, c = map(int, input().split())
        arr = list(map(int, input().split()))

        l = 1
        r = 10**9 # Max possible border width
 
        while l <= r:
            mid = (l + r) // 2
            total_area = 0

            for s in arr:
                # Calculate total area for current 'mid'
                total_area += (s + 2 * mid) ** 2
                # Optimization: break early if we exceed c to avoid huge numbers
                if total_area > c:
                    break

            if total_area == c:
                print(mid)
                break
            elif total_area > c:
                r = mid - 1
            else:
                l = mid + 1
    
if __name__ == "__main__":
    solve()