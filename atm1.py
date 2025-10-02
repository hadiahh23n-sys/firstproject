balance = 20000   # remove comma, otherwise it becomes a tuple
amount = 0
while(True):
    print("Your Balance: Rs", balance)

    print("\n\nMenu")
    print("---------------------")
    print(" 1. Deposit\n 2. Withdraw\n 3. Check Balance\n 4. Exit")

    choice = int(input("What service do you want: "))

    if choice == 1:
        print("How much money do you want to deposit?")
        amount = int(input("Enter Amount: "))
        balance += amount
        print("Your Current balance is:", balance)
        print("Your amount has been deposited successfully. Thank you.")

    elif choice == 2:
        print("How much money do you want to withdraw?")
        amount = int(input("Enter Amount: "))
       
        balance -= amount
        print("Your current balance is:", balance)
        print("Your amount has been withdrawn successfully. Thank you.")
        
    elif choice == 3:
        print("Your current balance is:", balance)

    elif choice == 4:
        print("You have exited. Thank you.")
        break

    else:
        print("Invalid choice!!!")
