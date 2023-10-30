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

#Write your code below this line 👇
running=True
c=0
d=0
while running:
  n=int(input("What do you want to choose? 0 for ROCK,1 for SCISSOR,2 for PAPER:-"))
  c=random.randint(0,2)
  #print(c)
  #d=[rock,scissors,paper]
  #e=d[c]
  #print(e)
  if n==0:
    print()
    print("Rock")
    print(rock)
    print("Computer Chooses:-")
    print()
    if(n==c):
      print("Rock")
      print(rock)
      print("DRAW")
    elif(c==1):
      print("Scissors")
      print(scissors)
      print("YOU WIN")
      c=c+1
    else:
      print("Paper")
      print(paper)
      print("YOU LOSE")
      d=d+1
  elif n==1:
    print()
    print("Scissors")
    print(scissors)
    print("Computer Chooses:-")
    print()
    if(n==c):
      print("Scissors")
      print(scissors)
      print("DRAW")
    elif(c==0):
      print("Rock")
      print(rock)
      print("YOU LOSE")
      d=d+1
    else:
      print("Paper")
      print(paper)
      print("YOU WIN")
      c=c+1
  elif n==2:
    print()
    print("Paper")
    print(paper)
    print("Computer Chooses:-")
    print()
    if(n==c):
      print("Paper")
      print(paper)
      print("DRAW")
    elif(c==0):
      print("Rock")
      print(rock)
      print("YOU WIN")
      c=c+1
    else:
      print("Scissors")
      print(scissors)
      print("YOU LOSE")
      d=d+1
  else:
    print("Wrong Choice")
  
  b=int(input("press 0 for stop and 1 for running:"))
  if(b==0):
    running=False
    print("Game Stopped")
    print(f"You won {c} times")
    print(f"You lose {d} times")
  elif(b==1):
    running=True
  else:
    print("Wrong choice")
    continue
