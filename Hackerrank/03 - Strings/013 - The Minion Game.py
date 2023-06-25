# https://www.hackerrank.com/challenges/the-minion-game/problem
# Score: 40

def minion_game(string):
    # your code goes here
    string = string.upper()
    vowel = "AEIOU"
    stuart_counter = 0
    kevin_counter = 0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin_counter += len(string[i:])
        else:
            stuart_counter += len(string[i:])
    if kevin_counter > stuart_counter:
        print(f"Kevin {kevin_counter}")
    elif kevin_counter < stuart_counter:
        print(f"Stuart {stuart_counter}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
