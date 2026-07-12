print("Welcome to Python Pizza Deliveries!")
bill=0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if size == "S":
    bill+=15
    if pepperoni == "Y":
        bill+=2
elif size == "M":
    bill+=20
    if pepperoni == "Y":
        bill+=3
elif size == "L":
    bill+=25
    if pepperoni == "Y":
        bill+=3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill+=1
print (f"Your final bill is: ${bill}.")
