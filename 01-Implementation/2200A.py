"""
Day 127: 2200A - Streak Saver Simulation
Topic: Simulation / Arrays / Fast I/O
Goal: Simulate decrement cycles from various starting positions to determine 
      unique final winning states.

Logic:
1. Fast I/O: Reads all input tokens at once using `sys.stdin.read().split()` to handle heavy test data efficiently.
2. Simulation Engine: For each starting position, copy the original array and simulate step-by-step 
   decrements in a round-robin fashion until the total sum reaches zero.
3. Winner Collection: Track the index that delivers the final reduction (`total == 0`) using a set, 
   then output the count of unique winning starting positions.

Complexity Analysis:
- Time: Depends on array values and size $N$, optimized via structured bulk reading.
- Space: $\mathcal{O}(N)$ to store input tokens, arrays, and output buffers.
"""

import sys

def solve():
    # Read the entire input buffer into memory once for blistering performance
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a_orig = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        winners = set()
        # Simulate game/reduction process from every possible start position
        for start in range(n):
            a = list(a_orig)
            total = sum(a)
            cur = start
            while total > 0:
                if a[cur] > 0:
                    a[cur] -= 1
                    total -= 1
                    if total == 0:
                        winners.add(cur)
                        break
                cur = (cur + 1) % n
        
        out.append(str(len(winners)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()