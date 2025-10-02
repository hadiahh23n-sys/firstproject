



print("Welcome to my calculator")
print("For addition : type 1 ")
print("For subtraction : type 2 ")
print("For multiplication : type 3 ")
print("For division : type 4 ")
choice=input("Enter the choice please: ")
x=input("Enter the first number please: ")
y=input("Enter the second number please: ")

if(x==1):
     print("Result :",x+y)
elif(x==2):
     print("Result :",x-y)
elif(x==3):
     print("Result :",x*y)
elif(x==4):
     print("Result :",x/y)
else:
     print("Invalid Number")
   