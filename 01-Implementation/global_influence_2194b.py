# Day 10: Global Influence (Codeforces 2194B)
# Folder: Implementation
# Logic: Global Pool Contribution. Each element contributes (i//x)*y.
# The final value of an element is its original value + (total pool - its own contribution).
# Time Complexity: O(n) - Two linear passes through the array.
# Space Complexity: O(n) - To store the individual contributions in a list.

import sys

# Faster I/O for competitive programming
input = lambda : sys.stdin.readline().rstrip()

def solve():
    # m: Number of test cases
    m_input = input()
    if not m_input: return
    m = int(m_input)

    for _ in range(m):
        # n: elements, x: threshold, y: contribution value
        n, x, y = map(int, input().split())
        s = list(map(int, input().split()))

        contri = []
        glo = 0

        # Pass 1: Build the global pool and track individual contributions
        for i in s:
            contribut = (i // x) * y
            contri.append(contribut)
            glo += contribut
        
        maxi = 0 
        
        # Pass 2: Calculate the "Boosted" value for each element and find the Max
        for t in range(n):
            # Element gets the total pool minus what it contributed itself
            curr_w = s[t] + (glo - contri[t])
            if curr_w > maxi:
                maxi = curr_w

        print(maxi)

if __name__ == "__main__":
    solve()