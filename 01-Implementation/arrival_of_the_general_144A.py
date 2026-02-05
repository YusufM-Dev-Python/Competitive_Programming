import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    min_val = min(arr)

    # 1. Tallest needs to be at index 0. We find the FIRST occurrence.
    max_in = arr.index(max_val)
    
    # 2. Shortest needs to be at index n-1. We find the LAST occurrence.
    min_in = 0
    for i in range(n):
        if arr[i] <= min_val:
            min_in = i
            
    # Calculate moves: max_in moves to the front, (n-1-min_in) moves to the back.
    answer = max_in + ((n - 1) - min_in)

    # If the max was to the right of the min, they swap once as they pass each other.
    # This reduces the total moves by 1.
    if max_in > min_in:
        answer -= 1  
        
    print(answer) 

if __name__ == "__main__":
    solve()