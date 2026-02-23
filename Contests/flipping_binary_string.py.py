"""
Day 21: Contest Problem B
Logic:
1. Count the occurrences of '1' and '0' in the binary string.
2. If count_ones is even:
   - Output all indices where the character is '1'.
3. Else if count_zeros is odd:
   - Output all indices where the character is '0'.
4. Otherwise, no valid construction exists, so output -1.

Complexity Analysis:
- Time: O(N) - Two passes for counting and one pass for index collection.
- Space: O(N) - To store the list of indices.
"""

import sys

# Faster I/O for competitive programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n = int(input())
        b = input()
        
        count_ones = b.count('1')
        count_zeros = b.count('0')
        
        # Priority 1: Even number of 1s
        if count_ones % 2 == 0:
            print(count_ones)
            indices = [str(i + 1) for i in range(n) if b[i] == '1']
            if count_ones > 0:
                print(" ".join(indices))
            else:
                print() # Handle edge case with zero ones
                
        # Priority 2: Odd number of 0s
        elif count_zeros % 2 != 0:
            print(count_zeros)
            indices = [str(i + 1) for i in range(n) if b[i] == '0']
            print(" ".join(indices))
            
        # Failure case
        else:
            print('-1')

if __name__ == "__main__":
    solve()