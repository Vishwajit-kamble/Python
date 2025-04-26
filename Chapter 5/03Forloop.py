nums = (1,4,9,25,36,49,64,81,100)
print("Enter number to search: ")
n = int(input())
idx = 0
for i in nums:
    if(i==n):
        print("Number",n,"Found! at idx",idx)
    idx+=1