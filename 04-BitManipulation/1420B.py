"""
Day 134: Codeforces 1420B - Rock and Lever
Topic: Bit Manipulation / Combinatorics
Logic:
1. Read the number of test cases `t`.
2. For each test case, read `n` and the array elements.
3. Track the frequency of each element's most significant bit position using `num.bit_length()`.
4. Two numbers can form a valid pair if their highest set bit is at the same position. For each bit length group with `num` elements, the number of valid pairs is given by the combination formula `num * (num - 1) // 2`.
5. Sum up the pairs across all bit lengths and print the total.

Complexity Analysis:
- Time: O(N) per test case - iterating through the input array once and the fixed-size 32-bit frequency array.
- Space: O(N) - to store the input array (and O(1) for the frequency array of size 32).
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        freq = [0] * 32
        total_pairs = 0

        for num in arr:
            freq[num.bit_length()] += 1

        for num in freq:
            total_pairs += (num * (num - 1)) // 2 

        print(total_pairs) 

if __name__ == "__main__":
    solve()