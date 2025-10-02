list=[4,9,65,34,25,67,22]

even=0
odd=0

for x in (list):

        if(x%2==0):
         print("Even: ",x)
         even+=1
        else:
         print("Odd:  ",x)
         odd+=1

print("TOTAL EVEN NUMBERS: ",even)
print("TOTAL ODD NUMBERS: ",odd)