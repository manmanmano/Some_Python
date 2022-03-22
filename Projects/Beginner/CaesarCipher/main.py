from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet += ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def to_caesar(text, shift, direction):
    result = ""
    for letter in text:
        if letter == ' ':
            result += letter
        else:
            position = alphabet.index(letter)
            if direction == 'encrypt':
                new_position = position + shift 
            else:
                new_position = position - shift
            result += alphabet[new_position]
    return result


print("\n", logo, "\n")
direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ").lower()
if direction == "encrypt" or direction == "decrypt":
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))
    result = to_caesar(text, shift, direction)
    print(f"\nThe converted text is: {result}\n")
else:
    print("No direction found, please try again.\n")
