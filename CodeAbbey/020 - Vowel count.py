#https://www.codeabbey.com/index/task_view/vowel-count

n = int(input())
rezultate = []
for i in range(n):
    string_line = input()
    rezultate.append(string_line.count("a") + string_line.count("e") + string_line.count("i") + string_line.count("o")
                     + string_line.count("u") + string_line.count("y"))

[print(rezultate[i], end=" ") for i in range(len(rezultate))]