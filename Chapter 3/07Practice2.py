# WAP to check if a list contain palindrome of elements 

list1 = [1,2,3,2,6]
copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("Palindrome")
else:
    print("Not Palindrome")