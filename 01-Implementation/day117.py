"""
Day 117: Constant Output Solution
Topic: Implementation / Math
Goal: Read input constraints and output the required fixed value efficiently.

Logic:
1. Input Handling: Consumes the input size token to maintain standard input sync.
2. Direct Output: Prints the computed fixed constant result (25) directly.
3. This avoids unnecessary memory allocation or iteration when the answer is invariant.

Complexity Analysis:
- Time: O(1) - Constant time execution.
- Space: O(1) - Constant auxiliary space.
"""

import sys

def main():
    # Read n from standard input to maintain standard I/O compliance
    input()
    print(25)

if __name__ == "__main__":
    main()