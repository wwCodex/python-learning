import random
#Name art not made by me
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

print('\n"But...."')

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

if alive:
    input("\nPress ENTER...")
    print("\nThe lights suddenly come back on.")
    print("\n...")
    input()
    print("Someone is standing in front of you.")
    input()
    print("\nA man wearing a black uniform.")
    print("A silver watch hangs from his pocket.")
    print("His face is strangely pale.")
    input()
    print('"Tickets, please."')
    input()

    if "Ticket" in inventory:
        print("\nYou hand over your ticket.")
        print('"Thank you."')

    else:
        print("\nYou search your pockets.")
        print("Nothing.")
        input()
        print('\nThe inspector smiles.')
        print('"Interesting..."')
        sanity -= 10

    input()
    print('\n"...What was your name?"')
    player = input("\nEnter your name: ")
    input()
    print(f'\n"...Ah yes, {player}."')
    input()
    print('"I have been expecting you."')
    sanity -= 5

if alive:
    input("\nPress ENTER...")
    print("\nYou notice one last door.")
    print("Unlike the others...")
    print("It is locked.")
    input()

    if silver_key:
        print("\nYou use the Silver Key.")
        input()
        print("Click.")
        print("The door slowly opens...")
        input()
        print("\nInside is a tiny room.")
        print("Dust covers everything.")
        input()
        print("\nThere is an old journal.")
        print("You begin reading...")
        input()
        print("\nEntry 1:")
        print('"The train crashed."')
        input()
        print("\nEntry 2:")
        print('"Nobody survived."')
        input()
        print("\nEntry 3:")
        print('"Except..."')
        input()
        print('"One passenger refuses to leave."')
        ghost_seen = True

    else:
        print("\nThe door won't open.")
        print("Maybe there's a key somewhere.")

if alive:
    input("\nPress ENTER...")
    print("\nAs you walk back...")
    input()
    print("\nEvery seat is occupied.")
    input()
    print("\nYou freeze.")
    input()
    print("The train was empty.")
    print("Just moments ago.")
    input()
    print("\nNobody speaks.")
    print("Nobody moves.")
    input()
    print("\nEvery passenger slowly turns...")
    input()
    print("...and looks directly at you.")
    sanity -= 20

if alive:
    event = random.randint(1, 3)

    if event == 1:
        print("\nA child laughs somewhere.")
        sanity -= 5

    elif event == 2:
        print("\nYou hear someone whisper your name.")
        sanity -= 10

    else:
        print("\nEverything is silent.")
        sanity += 5

if alive:

    input("\nPress ENTER...")
    print("\nA voice echoes through the train.")
    input()
    print('"Only ONE of you belongs here."')
    input()
    print("\nWho do you think is alive?")
    print("\n1. The little girl")
    print("2. The businessman")
    print("3. Me")
    truth = input("\nChoice: ")

if alive:
    print("\nThe train begins slowing down...")
    input()
    print("\nOutside...")
    print("There is a station.")
    input()
    print("\nBut the station has no name.")
    input()
    print("\nThe doors open.")

if alive and truth == "3" and girl_helped and silver_key and lever_stop and not money:
    print("\nThe station master steps onto the platform.")
    input()
    print('"You finally remembered."')
    input()
    print('"This train was never taking you to death..."')
    input()
    print('"It was bringing you back."')
    input()
    print("\nThe Silver Key begins glowing.")
    input()
    print("\nEverything around you starts fading.")
    input()
    print("\nYou suddenly wake up...")
    print("\n11:56 PM")
    print("You're back on the station bench.")
    input()
    print("\nA normal train arrives.")
    print("Its destination reads:")
    print("\nHOME")
    input()
    print("\nThe station master smiles.")
    print('"This time... take the right train."')
    input()
    print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    print("      TRUE ENDING")
    print(" The Last Train Never Came")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    alive = False

if alive and truth != "3":
    print("\nThe passengers begin laughing.")
    input()
    print('"Wrong answer."')
    input()
    print("\nYou look at your own reflection.")
    input()
    print("\nYou aren't there.")
    input()
    print("\nYou realize...")
    print("You died before boarding the train.")
    input()
    print("\nThe train doors close.")
    print("You remain inside forever.")
    print("\n👻 GHOST ENDING")
    alive = False

if alive and money:
    print("\nYou step off the train.")
    input()
    print("\nThe suitcase is still in your hand.")
    input()
    print("\nYou open it.")
    input()
    print("\nEvery note inside has turned into ash.")
    input()
    print("\nA whisper says...")
    print('"Greed always has a price."')
    input()
    print("\nYou hear a train whistle behind you.")
    print("When you turn around...")
    print("The platform is gone.")
    print("\n💰 GREEDY ENDING")
    alive = False

if alive and sanity <= 20:
    print("\nYou can't tell what is real anymore.")
    input()
    print("\nEvery passenger has your face.")
    input()
    print("\nThey all smile.")
    input()
    print("\nYou begin laughing.")
    input()
    print("\nThe train keeps moving forever.")
    print("\n😵 INSANITY ENDING")
    alive = False

if alive and not girl_helped:
    print("\nThe little girl walks past you.")
    input()
    print('"You left me alone..."')
    input()
    print("\nShe disappears into the fog.")
    input()
    print("\nThe station disappears with her.")
    input()
    print("\n👧 LOST CHILD ENDING")
    alive = False

if alive:
    print("\nThe black-uniformed conductor returns.")
    input()
    print('"Every train needs someone to guide it."')
    input()
    print("\nHe removes his cap.")
    input()
    print("He places it on your head.")
    input()
    print("\nThe whistle blows.")
    print("\nA new passenger arrives...")
    input()
    print("\nYou whisper:")
    print('"Tickets, please."')
    print("\n🚂 NEW CONDUCTOR ENDING")

print("\n=======================================")
print("GAME OVER")
print("=======================================")
print("\nFinal Inventory:")

for item in inventory:
    print("-", item)
print("\nFinal Sanity:", sanity)
print("\nThank you for playing...")
print("\nTHE LAST TRAIN")


