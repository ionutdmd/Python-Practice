# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Score: 20
from collections import defaultdict

n, m = map(int, input().split())
a_list = []
for _ in range(n):
    a_list.append(input())

b_list = []
for _ in range(m):
    b_list.append(input())

output_result = defaultdict(list)
for i in range(len(b_list)):
    if b_list[i] in a_list:
        for j in range(len(a_list)):
            if b_list[i] == a_list[j]:
                output_result[i].append(j+1)
    else:
        output_result[i].append(-1)

for result in output_result.items():
    print(" ".join(map(str, result[1])))




