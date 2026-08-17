import random 


def choose_liar():
    return random.randint(1, 3)


def show_story():
    print("""
================================
        THE INTERROGATION
================================

A diamond disappeared from a museum.

There were only three people inside:

1. Arthur - The Guard
2. Clara  - The Curator
3. James  - The Cleaner

One of them is lying.
You have ONE accusation.
""")


def interrogate(suspect, liar):

    if suspect == 1:
        if liar == 1:
            print('\nArthur: "I never entered the gallery tonight."')
        else:
            print('\nArthur: "I saw Clara near the gallery at 10 PM."')

    elif suspect == 2:
        if liar == 2:
            print('\nClara: "I left the museum before 9 PM."')
        else:
            print('\nClara: "James was cleaning the west hallway."')

    elif suspect == 3:
        if liar == 3:
            print('\nJames: "I did not see Arthur all night."')
        else:
            print('\nJames: "Arthur was guarding the main entrance."')

    else:
        print("\nThat suspect does not exist.")


def play_game():

    liar = choose_liar()

    show_story()

    questioned = []

    while len(questioned) < 3:

        suspect = int(input("\nWho do you want to question? (1/2/3): "))

        if suspect in questioned:
            print("You've already questioned them.")
            continue

        if suspect < 1 or suspect > 3:
            print("Choose 1, 2 or 3.")
            continue

        questioned.append(suspect)
        interrogate(suspect, liar)

    print("\nYou've heard all three statements.")

    accusation = int(input("Who is lying? (1/2/3): "))

    if accusation == liar:
        print("\nCASE CLOSED")
        print("You caught the liar.")

    else:
        print("\nCASE FAILED.")
        print(f"Suspect {liar} was actually lying.")


play_game()