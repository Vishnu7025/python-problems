#finding palindrome of a number using Slicing

string=input("Enter a string : ")
reverse_string=string[::-1]
if string==reverse_string:
    print("It is a palindrome")
else:
    print("not a palindrome")

#Using for loop

# string=input("Enter string ")
# reverse=""
# for i in string:
#     reverse=i + reverse
# print(reverse)
# if string == reverse :
#     print(reverse,"is a palindrome")
# else:
#     print(reverse,"is not a plaindrome")



