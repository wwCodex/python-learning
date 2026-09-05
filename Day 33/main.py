MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----"
}

REVERSE = {}
for key in MORSE:
    REVERSE[MORSE[key]] = key

def encode():
    text = input("\nEnter message: ").upper()

    result = []

    for letter in text:

        if letter == " ":
            result.append("/")

        elif letter in MORSE:
            result.append(MORSE[letter])

    print("\nEncoded:")
    print(" ".join(result))

def decode():
    code = input("\nEnter Morse: ").split()
    result = ""

    for symbol in code:

        if symbol == "/":
            result += " "

        elif symbol in REVERSE:
            result += REVERSE[symbol]

    print("\nDecoded:")
    print(result)
    

while True:

    print("""
    MORSE TRANSLATOR

1. Encode
2. Decode
3. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        encode()
    elif choice == "2":
        decode()
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option.")