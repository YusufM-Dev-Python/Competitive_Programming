import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    # s: list of coin values
    s = list(map(int, input().split()))
    
    # Greedy Choice: Sort descending to pick largest coins first
    s.sort(reverse=True)
    
    total = sum(s)
    coins = 0
    my_sum = 0
    
    for i in range(n):
        my_sum += s[i]
        coins += 1
        # Calculate what's left for the twin
        rem_sum = total - my_sum
        
        # We need strictly MORE than the twin
        if my_sum > rem_sum:
            break 
            
    print(coins)

if __name__ == "__main__":
    solve()