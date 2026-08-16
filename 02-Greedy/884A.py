"""
Day 129: 884A - Book Reading (Simulation & Fast I/O)
Topic: Simulation / Greedy
Goal: Determine the exact day when cumulative free time meets or exceeds 
      the required reading time 't'.

Logic:
1. Fast I/O: Bulk read all inputs at once via `sys.stdin.read().split()` to handle constraints efficiently.
2. Daily Free Time: Each day has 86,400 seconds. Subtract the time spent working (`a[day-1]`) 
   to get the free time available for reading.
3. Accumulation & Check: Accumulate free time daily and print the current day index 
   the moment total read time meets or exceeds `t`.

Complexity Analysis:
- Time: $\mathcal{O}(N)$ - Single linear scan through the days array.
- Space: $\mathcal{O}(N)$ to store input tokens.
"""

import sys

def solve():
    # Read the entire input buffer into memory once for fast execution
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    t = int(input_data[1])
    a = [int(x) for x in input_data[2:]]
    
    total_read = 0
    # Simulate day-by-day reading accumulation
    for day in range(1, n + 1):
        free_time = 86400 - a[day - 1]
        total_read += free_time
        if total_read >= t:
            print(day)
            break

if __name__ == '__main__':
    solve()