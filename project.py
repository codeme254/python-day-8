letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' ','', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '@', '$', '%', '&', '*', '+', '(', ')', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_string = ''
    for num in range(0, len(text)):
        current_letter = text[num]
        current_index = letters.index(current_letter)
        encrypted_string += letters[current_index + shift]
    print(f"The encoded text is {encrypted_string}")

def decrypt(text, shift):
    decrpyted_text = ''
    for num in range(0, len(text)):
        current_letter = text[num]
        current_index = letters.index(current_letter)
        decrpyted_text += letters[current_index - shift]
    print(f"the decrypted text is {decrpyted_text}")

if direction == 'encode':
    encrypt(text=text, shift=shift)
elif direction == 'decode':
    decrypt(text=text, shift=shift)


