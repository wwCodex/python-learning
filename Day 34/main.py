import random
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is fun when you build real projects.",
    "Discipline beats motivation every single day.",
    "Practice makes progress not perfection.",
    "Engineers solve problems one step at a time."
]


def calculate_accuracy(original, typed):
    correct = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1
    return (correct / len(original)) * 100


def calculate_wpm(text, seconds):
    words = len(text.split())
    minutes = seconds / 60
    if minutes == 0:
        return 0
    return words / minutes


def start_test():
    sentence = random.choice(sentences)
    print("           TYPERUSH")
    print("\nType the following sentence exactly:\n")
    print(sentence)
    input("\nPress Enter to start...")

    start = time.time()
    typed = input("\n> ")
    end = time.time()
    elapsed = end - start
    accuracy = calculate_accuracy(sentence, typed)
    wpm = calculate_wpm(typed, elapsed)
    print(f"Time Taken : {elapsed:.2f} seconds")
    print(f"WPM        : {wpm:.1f}")
    print(f"Accuracy   : {accuracy:.1f}%")

while True:

    start_test()
    again = input("\nTry another sentence? (y/n): ").lower()

    if again != "y":
        print("\nGoodbye!")
        break