# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Score: 10

number_of_elements = int(input())
my_set = set(map(int, input().split()))
number_of_operations = int(input())

for _ in range(number_of_operations):
    operation_command, *command_args = input().split()
    exec(f"my_set.{operation_command}({str(*command_args)})")
print(sum(my_set))
