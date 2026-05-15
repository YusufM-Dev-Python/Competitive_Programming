import sys
input = lambda:sys.stdin.readline().rstrip()

def solve():
    s,n = map(int,input().split())
    dragons = []
    for _ in range(n):
        x,y = map(int,input().split())
        dragons.append((x,y))

    dragons.sort(key = lambda d: d[0])
    for i,j in dragons:
        if s<=i:
            print("NO")
            return
        s+=j

    print("YES")

if __name__ == "__main__":
    solve()