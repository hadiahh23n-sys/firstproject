num = int(input("Enter any number up to which you want to find Prime Numbers: "))


for x in range(2,num+1):
      for i in range(2,x):
    
       if(x%i==0):
        break

      else:
         print(x, "is a Prime Number")
      


    
    