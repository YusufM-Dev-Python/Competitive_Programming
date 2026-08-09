"""
Day 123 (Part 2): 2256B - Binary Pattern Matching & Validation
Topic: Strings / Pattern Matching
Goal: Count how many predefined periodic binary patterns successfully match 
      the characters of the target string.

Logic:
1. Template Generation: Construct periodic patterns (`p1`, `p2`, `p3`, `p4`) truncated to string length `n`.
2. Validation Loop: Iterate through each template independently, verifying whether 
   non-wildcard characters in the target string `s` align with the pattern.
3. Accumulation: Increment the total valid pattern matches and output the final count.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear scan across the string for each of the fixed patterns.
- Space: $\mathcal{O}(N)$ to store the pattern templates and input string.
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

        total = 0

        # Define periodic pattern templates truncated to length n
        p1 = ("0110" * n)[:n]
        p2 = ("1001" * n)[:n]
        p3 = ("0011" * n)[:n]
        p4 = ("1100" * n)[:n]

        # Check pattern 1
        valid = True
        for i in range(n):
            if (s[i] == '0' or s[i] == '1') and s[i] != p1[i]:
                valid = False
                break
        if valid:
            total += 1

        # Check pattern 2
        valid = True
        for i in range(n):
            if (s[i] == '0' or s[i] == '1') and s[i] != p2[i]:
                valid = False
                break
        if valid:
            total += 1

        # Check pattern 3
        valid = True
        for i in range(n):
            if (s[i] == '0' or s[i] == '1') and s[i] != p3[i]:
                valid = False
                break
        if valid:
            total += 1
    
        # Check pattern 4
        valid = True
        for i in range(n):
            if (s[i] == '0' or s[i] == '1') and s[i] != p4[i]:
                valid = False
                break
        if valid:
            total += 1
            
        print(total)

if __name__ == "__main__":
    solve()