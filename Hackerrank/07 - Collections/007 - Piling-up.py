# https://www.hackerrank.com/challenges/piling-up/problem
# Score: 50

from collections import deque


def is_pilled(new_deque):
    compare_value = max(new_deque[0], new_deque[-1])
    while len(new_deque) > 0:
        if compare_value < new_deque[0] and compare_value < new_deque[-1]:
            return False
        if new_deque[0] <= compare_value and new_deque[-1] <= compare_value:
            if new_deque[0] >= new_deque[-1]:
                compare_value = new_deque.popleft()
            else:
                compare_value = new_deque.pop()
        elif new_deque[0] <= compare_value:
            compare_value = new_deque.popleft()
        else:
            compare_value = new_deque.pop()
    return True


T = int(input())
for _ in range(T):
    n = int(input())
    block_deque = deque(map(int, input().split()))
    if is_pilled(block_deque):
        print("Yes")
    else:
        print("No")
