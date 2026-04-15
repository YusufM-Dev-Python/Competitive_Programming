"""
Day 57: We Were Both Children (Codeforces 1850F)
Logic:
1. Count the frequency of each jump length. Frogs jumping further than N are ignored.
2. Create a 'trap_array' where trap_array[i] is the number of frogs that land on coordinate i.
3. For each jump length 'j' that has at least one frog:
   - Increment every multiple of 'j' up to N in the trap_array.
4. The complexity is O(N log N) because of the harmonic series sum.

Complexity Analysis:
- Time: O(N log N).
- Space: O(N) to store frequencies and trap counts.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)
        arr = list(map(int, input().split()))

        # Count frogs by their jump length
        freq = [0] * (n + 1)
        for x in arr:
            if x <= n:
                freq[x] += 1

        # Calculate how many frogs land on each coordinate [1...N]
        trap_array = [0] * (n + 1)
        for jump in range(1, n + 1):
            if freq[jump] > 0:
                # This inner loop is the "Harmonic" part
                for i in range(jump, n + 1, jump):
                    trap_array[i] += freq[jump]

        # The answer is the coordinate with the most frogs landing on it
        print(max(trap_array))

if __name__ == "__main__":
    solve()