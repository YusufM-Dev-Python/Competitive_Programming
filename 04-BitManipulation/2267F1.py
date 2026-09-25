import sys
input = lambda: sys.stdin.readline().rstrip()

def transform(b):
    m = len(b)
    xor_values = []

    for i in range(m):
        for j in range(i + 1, m):
            xor_values.append(b[i] ^ b[j])
            
    xor_values.sort()
    return xor_values[:m]

def solve():
    t_cases = int(input())
    for _ in range(t_cases):
        line = input().split()
        n = int(line[0])
        q = int(line[1])
        
        a = list(map(int, input().split()))
        
        queries = []
        for _ in range(q):
            queries.append(int(input()))
            
        history = [list(a)]
        curr_a = list(a)
        for _ in range(40):
            next_a = transform(curr_a)
            if next_a == curr_a:
                break
            history.append(next_a)
            curr_a = next_a
            
        answers = []
        for x in queries:
            idx = min(x, len(history) - 1)
            final_a = history[idx]
            ans = max(final_a) - min(final_a)
            answers.append(ans)
            
        for ans in answers:
            print(ans)

if __name__ == "__main__":
    solve()