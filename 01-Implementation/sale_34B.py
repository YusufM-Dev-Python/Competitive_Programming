import sys

# Fast I/O
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of TVs, m: max Bob can carry
    n, m = map(int, input().split())

    # Prices can be negative (profit) or positive (loss)
    arr = list(map(int, input().split()))
    
    # Greedy Choice: Sort to find the most negative prices first
    arr.sort()
    
    max_profit = 0

    for i in range(m):
        # Only take it if it's actually a negative price (profit)
        if arr[i] < 0:
            max_profit += abs(arr[i])
        else:
            # Since it's sorted, if this is 0 or positive, all others after are too
            break  
            
    print(max_profit)

if __name__ == "__main__":
    solve()