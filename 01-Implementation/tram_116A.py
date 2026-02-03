import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of stops
    n = int(input())
    
    max_cap = 0   # Records the highest passenger count seen so far
    curr_pas = 0  # Current number of people on the tram
    
    for _ in range(n):
        # a: people getting off, b: people getting on
        a, b = map(int, input().split())
        
        # Update current count: subtract those leaving, add those entering
        curr_pas = curr_pas - a + b
        
        # Check if the current count broke the previous record
        max_cap = max(max_cap, curr_pas)
        
    print(max_cap)

if __name__ == "__main__":
    solve()