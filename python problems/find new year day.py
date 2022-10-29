year = int(input("Enter a year: "))
nd = (year - 1) * 365
id = (year - 1)/4-(year - 1)/100+(year - 1)/400
td = nd + id
fd = td % 7
print(fd)
if (fd == 0):
    print('\n Monday')
elif(fd == 1):
    print('\n Tuesday')
elif(fd == 2):
    print('\n Wednesday')
elif(fd == 3):
    print('\n Thursday')
elif(fd == 4):
    print('\n Friday')
elif(fd == 5):
    print('\n Saturday')
elif(fd == 6):
    print('\n Sunday')



def number(num):
    d = num +10
    return d
d = number(10)
print(d)