# str1 = str(input('enter a sentence: '))
# mylist = str1.split()
# mylist = str1.split()[::-1]
# str2 =  " ".join(mylist)
# print(str2)

#after list comprehension
str1 = str(input('enter a sentense: '))
print( " ".join(str1.split()[::-1]))