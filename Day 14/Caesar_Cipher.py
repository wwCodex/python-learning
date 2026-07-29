def encrypt(original_text, shift_amount):
    final_text = ""
    for letter in original_text:
        if letter == " ":
            final_text += letter
        else :
            final_text+= alphabet[(alphabet.index(letter) + shift_amount)%26]

    print(final_text)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)