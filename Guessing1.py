number=25

print("**Welcome to Number Guessing Game**")
print("***Game Starts***")

guess=""
while(guess!=number):
    guess=int(input("\nGuess the number: "))

    if(guess<number):
        print("Too Low.Keep Trying!!!")
    elif(guess>number):
        print("Too High.Keep Trying!!!")
    else:
       print("Congratulations🥳.You did it✌🏻.")
     