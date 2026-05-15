"""
Day 77 (Bonus): Eating Candies (Codeforces 1669F)
Topic: Two Pointers
Logic:
1. Use two pointers starting at both ends of the array: 'l' (Alice) at 0 and 'r' (Bob) at n-1.
2. Track the cumulative candy weights eaten by Alice (sum_alice) and Bob (sum_bob).
3. Greedily move the pointers inward:
   - If sum_alice < sum_bob, Alice needs to eat more, so we advance 'l' and add to sum_alice.
   - If sum_bob < sum_alice, Bob needs to eat more, so we decrement 'r' and add to sum_bob.
   - If they are equal, we update 'max_candies' to the total count of candies consumed so far (l + (n - r - 1)), then have Alice eat another candy to keep the search moving.

Complexity Analysis:
- Time: O(N) - Linear scan using two pointers meeting in the middle.
- Space: O(1) - Auxiliary space beyond storing the input.
"""

import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        sum_alice = arr[0]
        sum_bob = arr[n-1]
        l = 0
        r = n-1

        max_candies = 0

        while l < r:
            if sum_alice == sum_bob:
                max_candies = (l + 1) + (n - r)
                # Keep moving inward
                l += 1
                r -= 1
                sum_alice += arr[l]
                sum_bob += arr[r]
            elif sum_alice < sum_bob:
                l += 1
                sum_alice += arr[l]
            else:
                r -= 1
                sum_bob += arr[r]
        
        print(max_candies)

if __name__ == "__main__":
    solve()