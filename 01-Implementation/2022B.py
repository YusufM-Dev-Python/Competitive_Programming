"""
Day 98: Pattern Constraint Check
Topic: Strings / Implementation
Logic:
1. The code differentiates logic based on whether the string length 'n' is even or odd.
2. For even lengths, it checks pairs (i, i+1) across the entire string.
3. For odd lengths, it enforces a constraint on the first character and then checks 
   the remaining pairs.
4. If a forbidden pattern ("aa" or "bb") is found in a pair, it flags the string 
   as impossible.

Complexity Analysis:
- Time: O(N) - Single pass through the string of length N.
- Space: O(1) - Minimal auxiliary space used.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        s = input()

        possible = True
        
        if n % 2 != 0:
            # Constraints for odd length strings
            if s[0] != 'a' and s[0] != '?':
                possible = False
            else:
                for i in range(1, n, 2):
                    pair = s[i:i+2]
                    if pair == "aa" or pair == "bb":
                        possible = False
                        break
        else:
            # Constraints for even length strings
            for i in range(0, n, 2):
                pair = s[i:i+2]
                if pair == "aa" or pair == "bb":
                    possible = False
                    break
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    solve()