balance = 20000
amount = 0
print("Welcome to the ATM !!")
print("Your Balance: Rs20,000")
while True:

    print("Menu")
    print("---------------------")
    print(" 1.Deposit\n 2.Withdraw\n 3.Check Balance\n 4.Exit")

    choice = int(input("Which service do you want: "))
    if choice == 1:
        print("How much money do you want to Deposit?")
        amount = int(input("Enter Amount: "))
        balance += amount
        print("Your Current balance is: ", balance)
        print("Your amount is deposited successfully.Thank You..")
    elif choice == 2:
        print("How much money do you want to Withdraw?")
        amount = int(input("Enter Amount: "))
        balance -= amount
        print("Your Current balance is: ", balance)
        print("Your amount is withdrawed  successfully.Thank You..")
    elif choice == 3:
        print("Your current Balance is : ", balance)
    elif choice == 4:
        print("You are exit.Thank You...")
        break
    else:
        print("Invalid choice!!!")
