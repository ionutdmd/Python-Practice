# https://www.hackerrank.com/challenges/nested-list/problem
# Score: 10

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
records.sort()
minim = min(scores)
for i in range(len(scores)):
    if scores[i] == minim:
        scores[i] = max(scores)
[print(item[0]) for item in records if item[1] == min(scores)]
