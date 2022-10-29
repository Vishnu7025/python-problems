start = int(input ("Enter you starting range: "))
end = int(input("Enter you end range: "))
print("prime numbers in the range",start,"to",end,"are")

for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if(i % j) == 0:
                break
        else:
            print(i)