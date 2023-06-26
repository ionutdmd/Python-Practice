# https://www.hackerrank.com/challenges/py-set-mutations/problem
# Score: 10

number_of_elements = int(input())
set_elements = set(map(int, input().split()))
number_of_operations = int(input())
for _ in range(number_of_operations):
    operation_command, set_length = input().split()
    operation_set = set(map(int, input().split()))
    exec(f"set_elements.{operation_command}({operation_set})")
print(sum(set_elements))
