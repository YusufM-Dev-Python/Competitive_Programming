import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    result = ""
    
    # 1-based indexing makes parity check (even/odd) intuitive
    for i in range(1, n + 1):
        # Odd layers start with "I love" (Wait, usually 1 is "I hate" in CF?)
        # Let's check: f(1)="I hate it", f(2)="I hate that I love it"
        # In your code: i=1 is "I love", i=2 is "I hate". 
        # Note: Usually CF asks for "I hate" first.
        if i % 2 == 0:
            result += "I love"
        else:
            result += "I hate"
        
        # Connector logic: "that" if more layers follow, "it" if it's the end
        if i != n:
            result += " that "
        else:
            result += " it"

    print(result)

if __name__ == "__main__":
    solve()