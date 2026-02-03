import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # a: Limak's weight, b: Bob's weight
    a, b = map(int, input().split())
    year = 0
    
    # Loop until Limak is strictly heavier than Bob
    while a <= b:
        a = a * 3  # Limak triples
        b = b * 2  # Bob doubles
        year += 1
        
    print(year)

if __name__ == "__main__":
    solve()