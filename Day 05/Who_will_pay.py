import random
#I solved this challenge a bit differently, using topics not yet covered and using a loop and user inputs to make it more interactive
#It's from the knowledge I have from my java lessons
ppl=int(input("How many people are in your group? "))
if ppl==0:
    print("Cheers mate, you're paying then")
    exit(0)
elif ppl<=0:
    print("....So there are less people now....sorry...who died?")
    exit(0)
n=0
frnds=[]
print ("Please write their names.\n")
while ppl>n:
    frnds.append(input())
    n+=1

num=random.randint(0,n-1)
print(f"{frnds[num]} Will pay the bill!!")
print(f"(Number randomised: {num})")