alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher_text(text, direction, shift):
    new_text = ""
    for letter in text:
        if letter.lower() in alphabet:
            # Handle the case of uppercase and lowercase letters
            index = alphabet.index(letter.lower())
            if direction == "encode":
                new_letter = alphabet[(index + shift) % 26]
            elif direction == "decode":
                new_letter = alphabet[(index - shift) % 26]
            # Preserve the case of the original letter
            if letter.isupper():
                new_text += new_letter.upper()
            else:
                new_text += new_letter
        else:
            # Append non-alphabetic characters unchanged
            new_text += letter
    print(f"The {direction} text is {new_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction in ["encode", "decode"]:
        text = input("Enter your text:\n")
        shift = int(input("Enter the shift value:\n"))
        cipher_text(text, direction, shift)

    else:
        print(f"Invalid direction! Please choose 'encode' or 'decode'.")

    continue_choice = input("Do you want to continue? Type 'yes' to continue or any other key to exit:\n").lower()
    if continue_choice != 'yes':
        print("Goodbye! Have a good day!")
        break
