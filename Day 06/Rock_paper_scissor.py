import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
r_p_c=[rock,paper,scissors]
while True:
 user_Choice = input("Rock, paper or scissors?")
 if user_Choice == "rock" or user_Choice == "Rock" or user_Choice == " rock" or user_Choice == " Rock":
        print(rock)
        num = 0
 elif user_Choice == "paper" or user_Choice == "Paper" or user_Choice == " paper" or user_Choice == " Paper":
        print(paper)
        num = 1
 elif user_Choice == "scissors" or user_Choice == "Scissors" or user_Choice == " scissors" or user_Choice == " Scissors":
        print(scissors)
        num = 2
 else:
     print("Invalid response")


 pc_choice = random.randint(0, 2)
 print(r_p_c[pc_choice])

 if pc_choice==num:
  print("Draw!!")
 elif pc_choice==0 and num==1:
  print("You win!")
  exit(0)
 elif pc_choice == 1 and num == 0:
  print("You lose!")
  exit(0)
 elif pc_choice == 1 and num == 2:
  print("You win!")
  exit(0)
 elif pc_choice == 2 and num == 1:
  print("You lose!")
  exit(0)
 elif pc_choice == 2 and num == 0:
  print("You win!")
  exit(0)
 elif pc_choice == 0 and num == 2:
  print("You lose!")
  exit(0)