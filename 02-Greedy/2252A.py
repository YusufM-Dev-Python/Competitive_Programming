"""
Day 121: 2252A - Contest Frequency Adjustment Logic
Topic: Greedy / Hash Maps
Goal: Compute the optimal sum of elements by evaluating frequency dominance and applying threshold adjustments.

Logic:
1. Frequency Mapping: Count the occurrences of each element in the array using a dictionary.
2. Dominant Element Identification: Find the most frequent element (`most_frequent_val`) and its count (`max_count`).
3. Threshold Condition: Check if the dominant element's frequency violates the balance condition `max_count > (n - max_count + 2)`.
4. Conditional Summation: If it exceeds the threshold, subtract the excess contribution from the total sum; otherwise, print the regular array sum.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ per test case - Linear passes to populate frequencies and calculate values.
- Space: $\mathcal{O}(N)$ to store array elements and frequency maps.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_input = input()
    if not t_input: return
    t = int(t_input)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        # Count frequencies of each element
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # Identify the most frequent element
        most_frequent_val = max(freq, key=freq.get)
        max_count = freq[most_frequent_val]

        # Apply greedy frequency threshold adjustment
        if max_count > (n - max_count + 2):
            print(sum(arr) - (most_frequent_val) * (max_count - (n - max_count + 2)))
        else:
            print(sum(arr))

if __name__ == "__main__":
    solve()