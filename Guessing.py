number=25

print("**Welcome to Number Guessing Game**")
print("***Game Starts***")

guess=""
while(guess!=number):
    guess=int(input("\nGuess the number: "))

    if(guess==number):
        print("Congratulations🥳.You did it✌🏻.")
    elif(guess>number):

        print("Too High.Keep Trying!!!")
    else:
        print("Too Low.Keep Trying!!!")
     