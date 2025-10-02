print("Welcome to sign-up page")
username = input("Set your username: ")
password = input("Set your password: ")

print("\nWelcome to login page")

for attempts in range(5):
    pwd = input("Enter your password: ")

    if pwd == password:
        print("✅ Successful login")
        print("Welcome, ",username)
        break
    else:
        print("❌ Wrong Password, TRY AGAIN 🎉")
else:
    print("🚫 Error: Too many incorrect attempts")
