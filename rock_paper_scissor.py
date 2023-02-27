# Importing the modules.
import random,sys
user_wins = 0
user_loss = 0
user_ties = 0
comp_wins = 0
comp_loss = 0
comp_ties = 0
# R -> Paper
# P -> Paper
# S -> Scissor
j = 0
# You can play 3 times if you want.
while (j < 3):
    print("Enter Player's name : ",end="")
    name = input().title()
    flag = 0
    i = 0
    # You have 5 turns to play.
    while(i<5):
        user = input("It's user's turn (R/P/S) : ")
        print("It's computer's turn : ",end="")
        computer = random.randint(1,3)
        if(computer == 1):
            turn = "R"
        elif(computer == 2):
            turn = "P"
        elif(computer == 3):
            turn = "S"
        print(turn)
        i += 1
        if((user == "R" and computer == 1) or (user == "P" and computer == 2) or (user == "S" and computer == 3)):
            user_ties += 1
            comp_ties += 1
        elif((user == "R" and computer == 3) or (user == "P" and computer == 1) or (user == "S" and computer == 2)):
            user_wins += 1
            comp_loss += 1
        elif((user == "S" and computer == 1) or (user == "R" and computer == 2) or (user == "P" and computer == 3)):
            user_loss += 1
            comp_wins += 1
    print("----------- S C O R E -----------")
    print("user score = ",user_wins)
    print("computer score = ",comp_wins)
    if(comp_wins < user_wins):
        print(name,", You wins the game.\n")
    elif(comp_wins > user_wins):
        print("Computer wins the match.\n")
    else:
        print("Match Ties.")
    print("You want to play again (Y/N) : ",end="")
    choice = input().upper()
    j += 1
    if(choice == "Y"):
        continue
    else:
        sys.exit()

