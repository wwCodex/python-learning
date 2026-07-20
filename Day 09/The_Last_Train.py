import random

print(r"""
████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗
   ██║   ██╔══██║██╔══╝
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

██╗      █████╗ ███████╗████████╗
██║     ██╔══██╗██╔════╝╚══██╔══╝
██║     ███████║███████╗   ██║
██║     ██╔══██║╚════██║   ██║
███████╗██║  ██║███████║   ██║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝

████████╗██████╗  █████╗ ██╗███╗   ██╗
╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║
   ██║   ██████╔╝███████║██║██╔██╗ ██║
   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║
   ██║   ██║  ██║██║  ██║██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
""")

print("=" * 70)
print("                 THE LAST TRAIN")
print("=" * 70)

print("\n11:57 PM")
print("Heavy rain pours outside.")
print("The station is almost empty.")

input("\nPress ENTER to continue...")

print("\nYou missed your usual train home.")
print("The next one arrives in three minutes.")

input("\nPress ENTER...")

print("\nAn old station master slowly walks towards you.")
print("His lantern flickers.")

print('\n"You are not supposed to be here tonight..."')

input("\nPress ENTER...")

print('\n"There is one train left."')

print('\n"But..."')

input()

print('\n"...do NOT board it."')

input("\nPress ENTER...")

print("\nYou look towards the tracks.")

print("\nNothing.")

print("Just darkness.")

input("\nPress ENTER...")

print("\nSuddenly...")

print("\nA whistle echoes through the station.")

print("\n████████████████████████████")

print("\nA train emerges from the fog.")

print("\nThe destination board reads:")

print("\n===============")
print("      END")
print("===============")

inventory = ["Phone"]
sanity = 100
alive = True
money = False
silver_key = False
ghost_seen = False
girl_helped = False
lever_stop = False
conductor = False

input("\nPress ENTER...")
print("\nWhat will you do?")
print("\n1. Board the train")
print("2. Listen to the station master")
print("3. Walk away")

choice = input("\nChoice: ").lower()
if choice == "1" or choice == "board":
    print("\nYou step onto the train.")
    print("The doors slam shut.")
    print("...")
    print("...")
    print("The train begins moving.")

elif choice == "2":
    print("\nThe old man sighs.")
    print('\n"I warned everyone."')
    print('"Nobody listens."')
    print('"If you see a little girl..."')
    input()
    print('"Do not let her cry."')
    print("\nHe hands you a silver coin.")
    inventory.append("Silver Coin")
    print("\nAdded to inventory!")
    input()
    print("\nCuriosity wins.")
    print("You board the train anyway.")
    print("The doors lock behind you.")

elif choice == "3":
    print("\nYou turn around.")
    print("You begin walking home.")
    input()
    print("\nAfter ten minutes...")
    print("...")
    print("...")
    print("You're back at the station.")
    print("\nThe train is still waiting.")
    print("\nThe station master is gone.")
    input()
    print("You slowly step onto the train.")

else:
    print("\nUnable to decide...")
    print("The train leaves without you.")
    print("\nENDING")
    print("The Coward")
    alive = False

if alive:
    input("\nPress ENTER...")
    print("\nThe train feels... wrong.")
    print("\nNo engine sound.")
    print("No conductor.")
    print("No announcements.")
    print("Only silence.")
    input()
    print("\nThree coaches are connected.")
    print("\n1. Coach A")
    print("2. Coach B")
    print("3. Engine Room")
    coach = input("\nWhere do you go? ").lower()

    if alive:

     if coach == "1" or coach == "a":
        print("\nYou slowly slide open the door.")
        input()
        print("\nThe coach is almost empty.")
        print("Rain taps against the windows.")
        print("One seat rocks back and forth...")
        input()
        print("\nA little girl sits alone.")
        print("She looks about eight years old.")
        print("She is drawing something.")
        input()
        print('\n"...Hello."')
        print("\nShe never looks up.")
        print("\nWhat do you do?")
        print("\n1. Sit beside her")
        print("2. Ask what she's drawing")
        print("3. Ignore her")
        girl = input("\nChoice: ").lower()

        if girl == "1":
            print("\nYou quietly sit beside her.")
            input()
            print('\nShe whispers...')
            print('"Nobody ever sits with me."')
            girl_helped = True
            sanity += 10
            input()
            print("\nShe smiles.")
            print("\nShe hands you a tiny silver key.")
            inventory.append("Silver Key")
            silver_key = True
            print("\nInventory:", inventory)

        elif girl == "2":
            print("\nShe turns the notebook towards you.")
            input()
            print("\nThe drawing shows...")
            print("\nTHIS TRAIN.")
            input()
            print("\nInside the train...")
            print("...someone is standing behind YOU.")
            input()
            print("\nYou quickly turn around.")
            print("Nobody.")
            sanity -= 15
            ghost_seen = True

        elif girl == "3":
            print("\nYou walk past her.")
            input()
            print("\nBehind you...")
            print("...you hear quiet crying.")
            sanity -= 10

        else:
            print("\nShe disappears.")
            sanity -= 20
        print("\nYou continue towards the next coach.")

if alive:
    if coach == "2" or coach == "b":
        print("\nCoach B smells like old paper.")
        input()
        print("\nA businessman is asleep.")
        print("A leather briefcase rests beside him.")
        print("\nWhat do you do?")
        print("\n1. Wake him")
        print("2. Open the briefcase")
        print("3. Leave quietly")
        man = input("\nChoice: ").lower()
        if man == "1":
            print("\nYou gently shake him.")
            input()
            print("\nHis eyes slowly open.")
            print('\n"...What year is it?"')
            input()
            print("\nBefore you can answer...")
            print("He suddenly vanishes.")
            ghost_seen = True
            sanity -= 10

        elif man == "2":
            print("\nInside the briefcase...")
            input()
            print("Stacks of money.")
            inventory.append("Money")
            money = True
            print("\nInventory:", inventory)
            print("\nAs you close it...")
            print("You hear footsteps behind you.")
            sanity -= 15

        elif man == "3":
            print("\nYou quietly leave him alone.")
            sanity += 5

        else:

            print("\nThe lights flicker.")

if alive:

    if coach == "3" or coach == "engine":
        print("\nYou enter the engine room.")
        input()
        print("\nNobody is driving.")
        print("Yet...")
        print("The train keeps moving.")
        input()
        print("\nThree levers sit before you.")
        print("\n1. STOP")
        print("2. REVERSE")
        print("3. FULL SPEED")
        lever = input("\nChoice: ").lower()

        if lever == "1" or lever == "stop":
            print("\nThe train violently shakes.")
            print("...")
            print("...then keeps moving.")
            lever_stop = True
            sanity -= 5

        elif lever == "2":
            print("\nThe lights suddenly turn red.")
            sanity -= 20

        elif lever == "3":
            print("\nThe train accelerates.")
            print("You almost fall.")
            sanity -= 10

        else:
            print("\nYou touch nothing.")

if alive:

    input("\nPress ENTER...")
    print("\nThe lights flicker.")
    input()
    print("...")
    input()
    print("...")
    input()
    print("Everything goes dark.")
    input()
    print("\nYour phone battery: 18%")
    print("\n1. Turn on flashlight")
    print("2. Walk in darkness")
    print("3. Stay still")
    dark = input("\nChoice: ").lower()

    if dark == "1":
        print("\nYour flashlight cuts through the darkness.")

        if random.randint(1, 4) == 2:
            print("\nSomeone is standing at the end of the coach.")
            input()
            print("...")
            print("They disappear.")
            sanity -= 20
            ghost_seen = True

        else:
            print("\nNothing happens.")

    elif dark == "2":
        print("\nYou walk blindly.")
        input()
        print("\nSomething brushes against your shoulder.")
        sanity -= 15

    elif dark == "3":
        print("\nYou don't move.")
        input()
        print("\nYou hear slow footsteps.")
        input()
        print("...")
        input()
        print("They stop.")

        sanity -= 10

    else:
        sanity -= 5

print("\n------------------------------")
print("Inventory:", inventory)
print("Sanity:", sanity)
print("------------------------------")

if sanity <= 0:
    print("\nYou begin laughing.")
    input()
    print("\nThe train was never haunted.")
    print("You were.")
    input()
    print("\nENDING")
    print("INSANITY")
    alive = False

