# #WAP to check Even or Odd
num = int(input("Enter the number : "))
if(num == 1):
    print("Natural Number !")
elif(num == 0 ):
    print("Nor Even Nor odd")
elif(num%2==0):
    print("The Number is Even !")
else: 
    print("The Number is Odd !")

# WAP to check greater among 3 numbers

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))
num4 = int(input("Enter the 4th number : "))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1,"Is Greater among all")
elif(num2>num3 and num2>num1 and num2>num4):
    print(num2,"Greater among all")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3,"Greater among all")
else:
    print(num4,"Greater among all")


#WAP to check multiple of 7 or not

num = int(input("Enter Number : "))
if(num%7==0):
    print(num," Is multiple of 7 !")
else:
    print(num," Is not multiple of 7 !")

