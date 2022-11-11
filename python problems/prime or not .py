num = int(input("Enter a positive number to check wheather it is prime or not:"))
if num > 1:
        for i in range(2,num):
            if (num % i)== 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
            
else:
    print(num,"is not a prme number")


#finding prime numbers between given two numbers

# for num in range(2,50):
#     for i in range(2,num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num,end=' ')





















