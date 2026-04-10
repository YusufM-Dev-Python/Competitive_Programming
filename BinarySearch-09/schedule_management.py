"""
Day 53: Schedule Management (Codeforces 1701C)
Logic:
1. Use Binary Search on Answer to find the minimum time 'mid'.
2. In 'mid' hours, each worker can:
   - Complete 'mid' tasks they are an expert in (1 hr/task).
   - Use remaining time to help with other tasks (2 hr/task).
3. If help_capacity (free_time // 2) >= leftovers (tasks exceeding mid),
   the time 'mid' is feasible. Try smaller time.
4. Otherwise, 'mid' is too small. Try larger time.

Complexity Analysis:
- Time: O(N * log(2*M)) - N is workers, log(2*M) is the search range.
- Space: O(N) - To store worker task counts.
"""

import sys

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Count tasks per worker
        counts = [0] * (n + 1)
        for worker_id in arr:
            counts[worker_id] += 1

        # Binary Search on the possible answer (Time in hours)
        low = 1
        high = 2 * m  # Absolute worst case: 1 worker does all m tasks (2 hrs each)
        best_time = high
        
        while low <= high:
            mid = (low + high) // 2  
            
            leftovers = 0
            help_capacity = 0
            
            for i in range(1, n + 1):
                expert_tasks = counts[i]
                
                if expert_tasks > mid:
                    # Worker can't finish their own expert tasks in 'mid' time
                    leftovers += (expert_tasks - mid)
                else:
                    # Worker has extra time to help others (takes 2 hours per task)
                    free_time = mid - expert_tasks
                    help_capacity += free_time // 2
            
            # Check if helpers can handle the leftovers
            if help_capacity >= leftovers:
                best_time = mid  
                high = mid - 1  # Try for a even smaller time
            else:
                low = mid + 1   # Need more time
                
        print(best_time)

if __name__ == "__main__":
    solve()