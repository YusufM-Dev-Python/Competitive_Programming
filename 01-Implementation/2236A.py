"""
Day 115: 2236A - Games on the Train (Fast I/O & Math Bounds)
Topic: Implementation / Math
Goal: Determine the minimum range parameter 'k' defined by the difference 
      between the maximum and minimum elements plus one for each test case.

Logic:
1. Fast I/O: Using `sys.stdin.read().split()` allows us to ingest all tokens 
   at once, drastically reducing overhead for multiple test cases.
2. Range Calculation: For each test case, we extract array `h` of size `n`. 
   The required span or bound condition is given by `max(h) - min(h) + 1`.
3. Collection: We store results in an output list and print them all at once 
   using a newline join for optimal performance.

Complexity Analysis:
- Time: O(N) total across all test cases - Linear scanning to find min and max elements.
- Space: O(N) to store the input tokens and output buffer.
"""

import sys

def solve():
    # Read all inputs from standard input at once for speed
    input_data = sys.stdin.read
    data = input_data().split()
    
    if not data:
        return

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Extract the array elements for the current test case
        h = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        min_h = min(h)
        max_h = max(h)
        
        # Calculate minimum k required based on the span
        k = max_h - min_h + 1
        out.append(str(k))
        
    # Print all answers separated by newlines
    print('\n'.join(out))

if __name__ == '__main__':
    solve()