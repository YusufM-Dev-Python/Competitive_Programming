import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    # Reading n and the array
    n = int(input())
    nums = list(map(int, input().split()))

    max_streak = 1
    curr_streak = 1

    # Single pass to check neighbors
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i+1]:
            curr_streak += 1
            # Update max_streak only when current one grows
            max_streak = max(max_streak, curr_streak)
        else:
            # Reset streak if the next number drops
            curr_streak = 1

    print(max_streak)

if __name__ == "__main__":
    solve()