import sys

# Fast I/O Template
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    event = list(map(int, input().split()))

    hired = 0 # Available police officers
    crime = 0 # Untreated crimes

    for i in event:
        # If the number is positive, it's a recruitment event
        if i > 0:
            hired += i
        
        # If it's -1, a crime has occurred
        if i == -1:
            if hired > 0:
                hired -= 1 # An officer is assigned to the crime
            else:
                crime += 1 # No officers available; crime goes untreated
                
    print(crime)

if __name__ == "__main__":
    solve()