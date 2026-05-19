"""
Day 79: Hulk (Codeforces 705A)
Topic: Implementation / Strings
Logic:
1. The feeling alternates between "I hate" on odd steps and "I love" on even steps.
2. We loop from 1 to n to build the string layers.
3. If it's not the final layer (i != n), we append " that " to connect to the next feeling.
4. If it is the final layer (i == n), we append " it" to close the sentence.

Complexity Analysis:
- Time: O(N) - Linear loop running 'n' times to construct the string.
- Space: O(N) - To store the resulting string segments.
"""

import sys

input = lambda:sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    result = ""
    for i in range(1, n + 1):
        # Odd layers are "I hate", even layers are "I love"
        if i % 2 != 0:
            result += "I hate"
        else:
            result += "I love"
        
        # Connectors: "that" if there's more coming, "it" if it's the end
        if i != n:
            result += " that "
        else:
            result += " it"

    print(result)

if __name__ == "__main__":
    solve()