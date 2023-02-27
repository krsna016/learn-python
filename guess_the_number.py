import random,sys
# You'll get a total of 6 turns to complete the game.
guess_num = random.randint(1,101)
count = 1
while count <= 6:
    print("I am guessing a number b/w 1 to 100 - Guess the number : ",end="")
    num = int(input())
    if(num == guess_num):
        print("Congratulation, You choose the correct number.\nYou have \
completed the game in "+count+" Guesses.")
        sys.exit()
    elif((guess_num - num) < 10 and (guess_num - num) > 0):
        print("Guess slightly Bigger number")
    elif((num - guess_num) < 10 and (num - guess_num) > 0):
        print("Guess Slightly Lower number")
    elif(num < guess_num):
        print("Number is too small")
    elif(num > guess_num):
        print("Number is too large")
    count += 1
print("Sorry, but the total turns are over. The guessed number is ",guess_num,".")

