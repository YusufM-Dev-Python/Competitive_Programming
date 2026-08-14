"""
Day 128: Array Parity and Zero Transformation Optimization
Topic: Greedy / Math / Fast I/O
Goal: Compute the minimum operations required to transform elements (zeros and negative ones) 
      under product/parity constraints.

Logic:
1. Fast I/O: Read all tokens at once using `sys.stdin.read().split()` to handle heavy test data efficiently.
2. Frequency Counting: Count the total number of zeros and negative ones (`-1`) in the array.
3. Operation Calculation:
   - Each zero requires 1 operation to change.
   - If the count of `-1`s is odd, an extra 2 operations are required to balance the parity.
4. Output Buffer: Append computed operations to a list and print all results joined by newlines.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear scan to count target elements.
- Space: $\mathcal{O}(N)$ to store input tokens and output buffers.
"""

import sys

def solve():
    # Read the entire input buffer into memory once for maximum speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        zeros = a.count(0)
        neg1 = a.count(-1)
        
        # Each zero requires 1 operation to become 1
        ops = zeros
        
        # If the count of -1s is odd, we need 2 operations to turn one -1 into 1
        if neg1 % 2 != 0:
            ops += 2
            
        out.append(str(ops))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()