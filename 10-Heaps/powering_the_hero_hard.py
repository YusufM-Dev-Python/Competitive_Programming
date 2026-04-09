"""
Day 52: Powering the Hero (Codeforces 1800C)
Logic:
1. We encounter bonus cards (arr[i] > 0) and heroes (arr[i] == 0).
2. Every time a hero appears, they take the strongest available bonus card.
3. A Max-Heap is the perfect data structure to always keep the maximum 
   value at the top with O(log N) efficiency.
4. Python's heapq is a min-heap, so we store negative values to simulate a max-heap.

Complexity Analysis:
- Time: O(N log N) - Each element is pushed and potentially popped once.
- Space: O(N) - To store the bonuses in the heap.
"""

import sys
import heapq

# Faster I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t_str = input()
    if not t_str: return
    t = int(t_str)
    
    for _ in range(t):
        n_str = input()
        if not n_str: continue
        n = int(n_str)
        arr = list(map(int, input().split()))
        
        total_power = 0
        heap = [] # This will act as our "pool" of bonus cards
        
        for i in range(n):
            if arr[i] > 0:
                # Push negative to simulate Max-Heap
                heapq.heappush(heap, -arr[i])
            elif arr[i] == 0:
                # Hero appears! If we have bonuses, take the biggest one
                if heap:
                    # Pop the smallest negative (which is the largest positive)
                    total_power += -heapq.heappop(heap)
        
        print(total_power)

if __name__ == "__main__":
    solve()