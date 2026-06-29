"""
Day 87 (Bonus): Sum of Round Numbers (Codeforces 1352A)
Topic: Implementation / Math
Logic:
1. A round number is a number of the form d * 10^k (a single non-zero digit followed by zeros).
2. We treat the input number 'n' as a string to easily inspect each digit and its position.
3. For each character/digit in the string, if it is not '0':
   - Its positional value is calculated by taking the digit and appending ('length - index - 1') zeros.
   - For example, in "5009" (length 4):
     - '5' at index 0 gets 4 - 0 - 1 = 3 zeros -> "5000"
     - '9' at index 3 gets 4 - 3 - 1 = 0 zeros -> "9"
4. Collect all such round components, count them, and format the output.

Complexity Analysis:
- Time: O(T * L) where T is the number of test cases and L is the number of digits (L <= 5 since n <= 10^4). This is extremely fast.
- Space: O(T * L) to buffer and print the results efficiently via sys.stdout.
"""

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = input_data[i]
        length = len(n)
        ans = []
        
        # Iterate through each digit and append its place value representation
        for index, digit in enumerate(n):
            if digit != '0':
                round_num = digit + '0' * (length - index - 1)
                ans.append(round_num)

        results.append(f"{len(ans)}\n{' '.join(ans)}")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()