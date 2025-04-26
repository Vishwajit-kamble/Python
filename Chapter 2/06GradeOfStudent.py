marks = int(input("Enter Marks : "))
if(marks >= 90):
    print("Grade = 'A'")
elif(marks>=80 and marks<=90):
    print("Grade = 'B'")
elif(marks>=70 and marks<=80):
    print("Grade = 'C'")
elif(marks<=70 and marks>=80):
    print("Grade = 'D'")
elif(marks<=35):
    print("Fail!!")