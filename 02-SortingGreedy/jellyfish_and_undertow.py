# Day 11: Jellyfish and Undertow (Codeforces 1875A)
# Folder: Greedy
# Logic: Capped Greedy. The timer (fuse) has a maximum capacity 'a'. 
# Each tool can increase the timer, but it can never exceed 'a'. 
# Since we use a tool when the timer is at least 1, the maximum 
# useful gain from any tool is a-1.
# Time Complexity: O(n) - Single pass through the tools array.
# Space Complexity: O(n) - Storing tool values.

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        # a: max timer value, b: initial timer, n: number of tools
        a, b, n = map(int, input().split())
        x = list(map(int, input().split()))

        # We start with the initial 'b' seconds.
        total_time = b
        
        for i in range(n):
            # For each tool, we can only gain up to a-1 seconds 
            # because the timer is capped at 'a'.
            total_time += min(x[i], a - 1)
            
        print(total_time)

if __name__ == "__main__":
    solve()