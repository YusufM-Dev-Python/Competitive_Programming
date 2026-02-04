import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # n: number of games played
    n = int(input())
    # s: string of results ('A' for Anton, 'D' for Danik)
    s = str(input())
    
    a = 0
    d = 0
    
    # Simple linear scan to count wins
    for i in range(n):
        if s[i] == 'A':
            a += 1
        else:
            d += 1
            
    # Decision logic
    if a > d:
        print("Anton")
    elif d > a:
        print("Danik")
    else:
        print("Friendship")
        
if __name__ == "__main__":
    solve()