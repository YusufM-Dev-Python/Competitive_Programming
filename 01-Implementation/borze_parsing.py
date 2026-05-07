"""
Day 72: Borze (Codeforces 32B)
Logic:
1. Iterate through the Borze code string using a pointer.
2. '.' -> 0 (increment index by 1)
3. '-.' -> 1 (increment index by 2)
4. '--' -> 2 (increment index by 2)
5. Continue until the end of the string.

Complexity Analysis:
- Time: O(N) - Single linear pass through the encoded string.
- Space: O(N) - Storing the result string.
"""

import sys

def solve():
    # Reading all at once is fine for Borze as the input is usually short
    borze_code = sys.stdin.read().strip()
    if not borze_code:
        return
        
    result = []
    i = 0

    while i < len(borze_code):
        if borze_code[i] == '.':
            result.append('0')
            i += 1
        elif borze_code[i] == '-':
            # The problem guarantees valid input, so i+1 will exist
            if borze_code[i+1] == '.':
                result.append('1')
            else:
                result.append('2')
            i += 2
            
    print("".join(result))

if __name__ == "__main__":
    solve()