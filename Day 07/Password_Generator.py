import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l_List=[]
n_List=[]
s_List=[]

n=0
for i in letters:
    l_List.append(letters[random.randint(0,len(letters)-1)])
    n+=1
    if n==nr_letters:
        break
m=0
for j in numbers:
    n_List.append(numbers[random.randint(0,len(numbers)-1)])
    m+=1
    if m==nr_numbers:
        break
p=0
for k in symbols:
    s_List.append(symbols[random.randint(0,len(symbols)-1)])
    p+=1
    if p==nr_symbols:
        break

pass_List=[]
f_List=s_List + n_List + l_List
while len(f_List)>0:
    indexer = random.randint(0, len(f_List) - 1)
    pass_List.append(f_List.pop(indexer))

print ("Your password is:","".join(pass_List))
