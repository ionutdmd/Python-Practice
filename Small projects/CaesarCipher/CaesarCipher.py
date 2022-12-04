from CipherArt import logo


def caesar(text, shift, direction):
    caesar_text = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % 26
            caesar_text += alphabet[new_index]
        else:
            caesar_text += char
    print(f"Your {direction}d result is: {caesar_text}")


def repeat():
    answer = input("Restart CaesarCipher? (type yes or no)").lower()
    return answer


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
while True:
    direction = input("Input 'encode' for encription, input 'decode' for decription:\n")
    text = input("Your message is: \n").lower()
    shift = int(input("Input shift number:\n"))
    caesar(text, shift, direction)

    if repeat() == 'no':
        break
