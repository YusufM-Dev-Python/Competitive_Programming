import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, t = map(int, input().split())
    queue = list(input())

    for _ in range(t):
        i = 0
        while i < n - 1:
            if queue[i] == 'B' and queue[i+1] == 'G':
                queue[i], queue[i+1] = queue[i+1], queue[i]
                # Swap happens, skip the girl we just moved past
                i += 2
            else:
                i += 1
    print("".join(queue))

if __name__ == "__main__":
    solve()