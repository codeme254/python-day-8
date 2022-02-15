letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', ' ','', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '@', '$', '%', '&', '*', '+', '(', ')', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        final_text = ''
        if shift > len(letters):
            shift %= len(letters)
        for num in range(0, len(text)):
            current_letter = text[num]
            current_index = letters.index(current_letter)
            if direction == 'encode':
                final_text += letters[current_index + shift]
            elif direction == 'decode':
                final_text += letters[current_index - shift]
        print(f"The {direction}d text is {final_text}")

    caesar(text=text, direction=direction, shift=shift)
    do_again = input("Do you want to go again? Type yes or no\n").lower()
    if do_again == 'no':
        go_again = False
        print("GoodBye👋👋🙌🙌")
    else:
        go_again = True