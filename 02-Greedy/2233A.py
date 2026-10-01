"""
Day 146: Codeforces 2233A - Greedy / Simulation / Math
Topic: Math / Case Analysis / Greedy
Logic:
1. Fast I/O is used to read all tokens at once.
2. For each test case, read target `n`, base rate `x`, secondary rate `y`, and AI setup time `z`.
3. Compute `time_no_ai` by combining both rates without AI setup: `ceil(n / (x + y))`.
4. Compute `time_ai` by evaluating whether spending `z` hours on AI setup is worth it:
   - If AI finishes the entire task during setup (`x * z >= n`), time is just the setup duration needed to hit `n`.
   - Otherwise, account for lines written during setup (`x * z`), then finish the remaining lines at the boosted combined speed (`x + 10 * y`).
5. Take the minimum time between the two options and store the result.

Complexity Analysis:
- Time: O(1) per test case - constant time mathematical calculations.
- Space: O(N) - to store input and output tokens.
"""

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        z = int(data[idx + 3])
        idx += 4

        # Option 1: Without AI
        # Combined speed = x + y, time = ceil(n / (x + y))
        time_no_ai = (n + x + y - 1) // (x + y)

        # Option 2: With AI setup for z hours
        if x * z >= n:
            time_ai = (n + x - 1) // x
        else:
            remaining_lines = n - x * z
            combined_speed_ai = x + 10 * y
            time_ai = z + (
                remaining_lines + combined_speed_ai - 1
            ) // combined_speed_ai

        ans = min(time_no_ai, time_ai)
        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()