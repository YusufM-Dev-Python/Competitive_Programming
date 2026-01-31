import sys

# Faster input reading for Competitive Programming
input = lambda: sys.stdin.readline().rstrip()

def solve():
    try:
        line = input()
        if not line: 
            return
        w = int(line)
        
        # Logic: Both parts must be even. 
        # Even + Even = Even (w % 2 == 0)
        # Smallest even part is 2, so w must be at least 2 + 2 = 4
        if w % 2 == 0 and w > 2:
            print("YES")
        else:
            print("NO")
    except ValueError:
        pass 

if __name__ == "__main__":
    solve()