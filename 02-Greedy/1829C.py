import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        INF = 10**9
        min10 = INF
        min01 = INF
        min11 = INF
        
        for _ in range(n):
            m, s = input().split()
            m = int(m)
            
            if s == '10':
                min10 = min(min10, m)
            elif s == '01':
                min01 = min(min01, m)
            elif s == '11':
                min11 = min(min11, m)

        ans = min(min11, min10 + min01)
        if ans < INF:
            print(ans)
        else:
            print(-1)

if __name__ == "__main__":
    solve()