import random

def random_of_ranges(*ranges):
    all_ranges = sum(ranges, [])
    return random.choice(all_ranges)


print("Welcome to Password Generator")
letter_number = int(input("How many letters do you want in your password? "))
numbers_number = int(input("How many numbers do you want in your password? "))
special_number = int(input("How many special characters do you want in your password? "))

password = []
for i in range(letter_number):
    password.append(chr(random_of_ranges(list(range(65, 91)), list(range(97, 123)))))

for i in range(numbers_number):
    password.append(chr(random.randint(48, 57)))

for i in range(special_number):
    password.append(chr(random.randint(33, 43)))

random.shuffle(password)
print("Your generated password is:")
[print(char, end='') for char in password]
