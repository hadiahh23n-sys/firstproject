print("Welcome to sign-up page")
username = input("Set your username: ")
password = input("Set your password: ")

print("Welcome to login page")
pwd =""
while pwd != password:
    pwd = input("Please enter your password: ")

print("Welcome,",username)