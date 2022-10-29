# normal way

# a=5
# b = 6
# c = a**b
# print(c)


# def power(x,y):
#     result = 1
#     while x != 0:
#         result *= y
#         x-=1
#     print("power of x: {}".format(result))

# power(4,4)

# Finding  Power without using multiplication(*) and division(/) operators
# Using nested loops
# For example to calculate 5^6. 
# 1) First 5 times add 5, we get 25. (5^2) 
# 2) Then 5 times add 25, we get 125. (5^3) 
# 3) Then 5 times add 125, we get 625 (5^4) 
# 4) Then 5 times add 625, we get 3125 (5^5) 
# 5) Then 5 times add 3125, we get 15625 (5^6) 

# def pow(a,b):
#     if(b==0):
#         return 1
         
#     answer=a
#     increment=a
     
#     for i in range(1,b):
#         for j in range (1,a):
#             answer+=increment
#         increment=answer
#     return answer

# print(pow(5,6))

# Method 2 (Using Recursion): Recursively add a to get the multiplication of two numbers. And recursively multiply to get a raise to the power b.


# def pow(a,b):
     
#     if(b):
#         return multiply(a, pow(a, b-1));
#     else:
#         return 1;
      
# # A recursive function to get x*y *
# def multiply(x, y):
     
#     if (y):
#         return (x + multiply(x, y-1));
#     else:
#         return 0;
 
# # driver program to test above functions *
# print(pow(5, 6));

