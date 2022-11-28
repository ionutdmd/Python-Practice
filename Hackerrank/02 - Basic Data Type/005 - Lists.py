# https://www.hackerrank.com/challenges/python-lists/problem
# Score: 10

if __name__ == '__main__':
    N = int(input())

list = []
for i in range(N):
    input_list = input().split()
    if input_list[0] == 'insert':
        list.insert(int(input_list[1]), int(input_list[2]))
    elif input_list[0] == 'print':
        print(list)
    elif input_list[0] == 'remove':
        list.remove(int(input_list[1]))
    elif input_list[0] == 'sort':
        list.sort()
    elif input_list[0] == 'append':
        list.append(int(input_list[1]))
    elif input_list[0] == 'pop':
        list.pop()
    elif input_list[0] == 'reverse':
        list.reverse()

