"""
Day 124: 2236D - Game Theory & Chain Parity Simulation
Topic: Arrays / Sorting / Game Theory
Goal: Analyze contiguous value chains with gap limits ('k') and simulate game move 
      parities to determine winning outcomes.

Logic:
1. Fast I/O & Sorting: Bulk read input using `sys.stdin.read().split()` and sort the array 
   via Timsort to group elements.
2. Frequency Extraction: Manually build unique values and their respective counts in linear time.
3. Chain Segmentation: Partition unique elements into isolated chains where adjacent elements 
   do not exceed gap limit `k`.
4. Parity Evaluation: Simulate choices within each chain by tracking odd counts (`current_odds`) 
   to determine winning configurations.

Complexity Analysis:
- Time: $\mathcal{O}(N \log N)$ per test case due to sorting the array tokens.
- Space: $\mathcal{O}(N)$ to store input tokens, unique values, counts, and output buffer.
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
        k = int(input_data[idx+1])
        idx += 2
        
        arr = list(map(int, input_data[idx : idx + n]))
        idx += n
        
        arr.sort()
        
        unique_vals = []
        counts = []
        
        # Build frequencies manually from the sorted array in O(N)
        for val in arr:
            if not unique_vals or unique_vals[-1] != val:
                unique_vals.append(val)
                counts.append(1)
            else:
                counts[-1] += 1
                
        possible = False
        U = len(unique_vals)
        chain_start = 0
        
        # Simulate chains without building new lists in memory
        while chain_start < U:
            chain_end = chain_start
            total_odds = counts[chain_start] % 2
            
            # Find the boundary of the current chain based on gap limit k
            while chain_end + 1 < U and unique_vals[chain_end + 1] - unique_vals[chain_end] <= k:
                chain_end += 1
                total_odds += counts[chain_end] % 2
                
            # Test move parities within this isolated chain bounds
            for i in range(chain_start, chain_end + 1):
                current_odds = total_odds
                
                # O(1) Parity adjustment for removing unique_vals[i]
                if counts[i] % 2 == 0:
                    current_odds += 1  # Even becomes odd
                else:
                    current_odds -= 1  # Odd becomes even
                    
                if current_odds > 0:
                    possible = True
                    break
                    
            if possible:
                break
                
            # Jump to start the next isolated chain
            chain_start = chain_end + 1
            
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()