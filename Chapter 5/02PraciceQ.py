#Print 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# print 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# Print multiplication table upto n
# n = int(input("Enter number: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

#print the below list using loops
# numbers = [1,4,9,25,36,49,64,81,100]
# i=1
# while i<=10:
#     print(i*i)
#     i+=1
# idx = 0
# while idx<len(numbers):
#     print(numbers[idx])
#     idx+=1

#Search the number x in the tupple
nums = (1,4,9,25,36,49,64,81,100)
x = int(input("Enter which number to search: "))
idx = 0
while idx<len(nums):
    if(nums[idx]==x):
        print("The Number",x,"Exist at index",idx)
        break
    else:
        print("The Number",x,"Doesn't Exist at index",idx)
        
    idx+=1