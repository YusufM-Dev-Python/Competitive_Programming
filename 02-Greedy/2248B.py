"""
Day 116 (Part 2): 2248B - Structural Bounds and Wall Validation
Topic: Sorting / Greedy / Fast I/O
Goal: Validate if array elements from 'b' can be properly bounded by segments 
      derived from array 'a' under strict size and relative positioning rules.

Logic:
1. Fast I/O: Reads all input tokens at once using `sys.stdin.read().split()` to prevent bottlenecks.
2. Initial Pruning: 
   - Checks if 'n' is at least double 'm' (`n < 2 * m`).
   - Validates global extrema: minimum of 'a' must not exceed minimum of 'b', 
     and maximum of 'b' must not exceed maximum of 'a'.
3. Sorting & Walls: Sorts both arrays and partitions array 'a' into left and right 
   subsegments (`left_wall` and `right_wall`) of size 'm'.
4. Positional Check: Iterates through to ensure elements of `b` fall strictly within 
   the corresponding left and right wall boundaries.

Complexity Analysis:
- Time: $\mathcal{O}(N \log N + M \log M)$ per test case due to sorting the arrays.
- Space: $\mathcal{O}(N + M)$ to store input tokens and partitioned arrays.
"""

import sys

def solve():
    # Read all tokens efficiently from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        a = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        b = [int(x) for x in input_data[idx : idx + m]]
        idx += m

        # Quick pruning conditions based on size and global extremes
        if n < 2 * m or min(a) > min(b) or max(b) > max(a):
            out.append("NO")
            continue
            
        a.sort()
        b.sort()
        
        # Partition array 'a' into left and right boundaries
        left_wall = a[:m]
        right_wall = a[-m:]
        
        possible = True
        for i in range(m):
            if not (left_wall[i] < b[i] < right_wall[i]):
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == "__main__":
    solve()