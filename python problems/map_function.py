def multipy(n):
    return n%2==0

number = [1,2,3,4,]
result = filter(multipy,number)
print(list(result))
