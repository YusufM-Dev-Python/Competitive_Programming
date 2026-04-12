"""
Day 55: Traffic Light (Codeforces 1742C)
Logic:
1. The traffic light is a cycle. To handle this, double the string (s + s).
2. We need the maximum time to wait for a 'g' (green) starting from color 'c'.
3. Scan the doubled string from right to left. 
4. Keep track of the most recent 'g' index (last_g).
5. Whenever we hit color 'c', the wait time is (last_g - current_index).
6. The maximum of these wait times is the answer.

Complexity Analysis:
- Time: O(N) - Single linear scan of the doubled string.
- Space: O(N) - Storing the doubled string.
"""

import sys

# Faster I/O for contest performance
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        # Read n and the current color c
        line = input().split()
        if not line: continue
        n, c = line[0], line[1]
        n = int(n)

        s = input()
        
        # If we are already at green, wait time is 0
        if c == 'g':
            print(0)
            continue

        # Doubling handle the circular nature
        s = s + s

        max_time = 0
        last_g = -1

        # Scan backwards to find the distance to the 'next' green light
        for i in range(2 * n - 1, -1, -1):
            if s[i] == 'g':
                last_g = i
            
            # If we find our color, calculate distance to the nearest future green
            if s[i] == c and last_g != -1:
                wait_time = last_g - i
                if wait_time > max_time:
                    max_time = wait_time

        print(max_time)

if __name__ == "__main__":
    solve()