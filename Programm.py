
print("This is Grading System!!")

marks=int(input("Enter your Marks:  "))



if(marks<0):
 print("Enter appropriate marks between (0-100)")
elif(marks>100):
 print("Enter appropriate marks between (0-100)")

elif(marks>=90):
 print("Your Grade is 'A'.")
elif(marks>=80):
 print("Your Grade is 'B'.")
elif(marks>=70):
 print("Your Grade is 'C'.")
elif(marks>=60):
 print("Your Grade is 'D'.")
elif(marks>=50):
 print("Your Grade is 'E'.")

else:
 print("Your Grade is 'F'.")

