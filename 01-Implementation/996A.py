"""
Day 86: Hit the Lottery (Codeforces 996A)
Topic: Greedy
Logic:
1. To minimize the total number of bills, we should greedily use the largest denominations 
   whenever possible.
2. The available denominations are 100, 20, 10, 5, and 1.
3. We loop through each bill size in descending order:
   - The number of bills of the current denomination we can use is calculated via integer division (n // bill).
   - The remaining balance to be cleared is updated using the modulo operator (n %= bill).

Complexity Analysis:
- Time: O(1) - The number of denominations is fixed at 5, so the loop runs a constant number of times.
- Space: O(1) - Minimal static memory used for tracking count and remaining amount.
"""

import sys

def solve():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # Available denominations in descending order
    denominations = [100, 20, 10, 5, 1]
    count = 0
    
    # Greedy approach: take as many of the largest bills as possible
    for bill in denominations:
        count += n // bill  # Add the number of bills of this denomination
        n %= bill           # Update n to the remaining amount
        
    print(count)

if __name__ == '__main__':
    solve()