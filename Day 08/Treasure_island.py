import random

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_.""  ,. .` ` `` ,  `"=._"=._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
*******************************************************************************
''')

print("🏝️ Welcome to Treasure Island!")
print("Your mission is to find the legendary Heart of Atlantis.\n")

inventory = []
luck = 100

#FIRST CHOICE 

print("You arrive at the island.")
print("Where do you want to go?")
print("1. Jungle 🌳")
print("2. Cave 🕳")
print("3. Beach 🏖")

choice1 = input("Choose: ").lower()

alive = True
won = False

if choice1 == "1" or choice1 == "jungle":

    print("\nThe jungle is thick and silent...")
    print("1. Climb a tree")
    print("2. Investigate the growling")
    print("3. Run")

    jungle = input("Choose: ").lower()

    if jungle == "1":
        print("\n🐵 A wise monkey gives you an Ancient Key!")
        inventory.append("key")
        luck += 20

    elif jungle == "2":
        print("\n🐯 A tiger was waiting.")
        print("GAME OVER.")
        alive = False

    elif jungle == "3":
        print("\nYou escape safely but learn nothing.")
        luck -= 10

    else:
        print("\nYou got lost.")
        alive = False


elif choice1 == "2" or choice1 == "cave":

    print("\nThe cave is pitch black.")
    print("1. Light a torch")
    print("2. Walk blindly")
    print("3. Shout")

    cave = input("Choose: ").lower()

    if cave == "1":
        print("\nYou discover ancient carvings.")
        print("One symbol is circled: 🐢")
        inventory.append("torch")

    elif cave == "2":
        print("\nYou fall into a pit.")
        alive = False

    elif cave == "3":
        print("\nThousands of bats chase you out!")
        luck -= 15

    else:
        alive = False


elif choice1 == "3" or choice1 == "beach":

    print("\nA pirate ship rests nearby.")
    print("1. Sneak aboard")
    print("2. Talk to pirates")
    print("3. Swim")

    beach = input("Choose: ").lower()

    if beach == "1":
        print("\nYou steal a treasure map!")
        inventory.append("map")

    elif beach == "2":
        if random.randint(1,2) == 1:
            print("\nThe pirates like you.")
            inventory.append("coin")
        else:
            print("\nThe pirates shoot you.")
            alive = False

    elif beach == "3":
        print("\n🦈 A shark eats you.")
        alive = False

    else:
        alive = False

else:
    print("You wandered into the ocean somehow.")
    alive = False

#TEMPLE

if alive:

    print("\nAfter hours of walking, you reach the Temple.")
    print("Three symbols appear.")

    print("🐍 Snake")
    print("🦅 Eagle")
    print("🐢 Turtle")

    symbol = input("Choose: ").lower()

    if symbol == "turtle" or symbol == "🐢":
        print("\nThe door slowly opens...")
    else:
        print("\nPoison darts shoot from the walls!")
        alive = False

#TUNNELS

if alive:

    print("\nInside are three tunnels.")

    print("1. Gold")
    print("2. Blue")
    print("3. Black")

    tunnel = input("Choose: ").lower()

    if tunnel == "1":

        print("\nTwo treasure chests appear.")

        print("1. Small")
        print("2. Large")

        chest = input("Choose: ").lower()

        if chest == "1":
            print("\nThe chest contains a crystal compass.")
            inventory.append("compass")

        else:
            print("\nIt was a mimic!")
            alive = False

    elif tunnel == "2":

        print("\nAn underground river blocks your way.")

        print("1. Swim")
        print("2. Follow the river")

        river = input("Choose: ").lower()

        if river == "1":
            print("\nYou barely survive.")
            luck -= 20

        else:
            print("\nYou discover a hidden bridge.")
            inventory.append("bridge pass")

    elif tunnel == "3":

        print("\nA sleeping dragon lies ahead.")

        print("1. Steal the key")
        print("2. Attack")
        print("3. Walk quietly")

        dragon = input("Choose: ").lower()

        if dragon == "1":
            print("\nYou steal the Dragon Key!")
            inventory.append("dragon key")

        elif dragon == "2":
            print("\nThe dragon wakes.")
            alive = False

        else:
            print("\nYou escape unnoticed.")

#FINAL ROOM

if alive:

    print("\nAt last...")
    print("The Heart of Atlantis rests on a pedestal.")

    print("Choose one object:")

    print("1. Golden Crown")
    print("2. Crystal Orb")
    print("3. Rusty Compass")

    final = input("Choose: ").lower()

    if final == "3":

        if "key" in inventory:
            print("\n🏆 SECRET ENDING!")
            print("The Ancient Key unlocks the compass.")
            print("It points to the REAL Heart of Atlantis!")
            print("You become the greatest treasure hunter ever.")
            won = True

        elif "map" in inventory:
            print("\n🏴‍☠️ ENDING 2")
            print("The map was fake.")
            print("Pirates steal the treasure before you.")
            print("You survive... but return empty-handed.")

        else:
            print("\n🏆 ENDING 1")
            print("The compass reveals the hidden treasure!")
            print("You escape rich!")

    elif final == "2":
        print("\n💀 ENDING 3")
        print("The Orb was cursed.")
        print("You are turned into stone.")

    else:
        print("\n💀 ENDING 4")
        print("The crown triggers the collapse of the temple.")
        print("You are buried forever.")

#STATS

print("\n----------------------")
print("Inventory:", inventory)
print("Luck:", luck)

if won:
    print("Status: LEGENDARY VICTORY 👑")
elif alive:
    print("Status: You survived.")
else:
    print("Status: Dead.")