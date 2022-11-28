# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    maxim = max(arr)
    for i in range(0, n):
        if arr[i] == maxim:
            arr[i] = min(arr)

    print(max(arr))
