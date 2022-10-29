# Program to print find next palindrome
# number greater than given number.
# function to check a number is
# palindrome or not1

# def isPalindrome(num):
#   # Declaring variables
#   # storing num in n so that we can compare it later
#     n = num
#     rev = 0

#     # while num is not 0 we find its reverse and store
#     # in rev
#     while (num > 0):
#         k = num % 10
#         rev = (rev * 10) + k
#         num = num // 10

#     # check if num and its reverse are same
#     if (n == rev):
#         return True
#     else:
#         return False

# # input number
# num = int(input('enter numbers: '))
# # start check from next num;
# num = num + 1
# # Loop checks all numbers from given no.
# # (num + 1) to next palindrome no.
# while (True):
#     if (isPalindrome(num)):
#         break
#     num = num + 1

# # printing the next palindrome
# print("Next Palindrome :")
# print(num)



def isPalindrome(num):
    n = num
    rev = 0
    while (num > 0):
        k = num % 10
        rev = (rev * 10) + k
        num = num // 10
    if (n == rev):
        return True
    else:
        return False
num = int(input('enter numbers: '))
num = num + 1
while (True):
    if (isPalindrome(num)):
        break
    num = num + 1
print("Next Palindrome :",num)
