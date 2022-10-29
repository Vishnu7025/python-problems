# l = ['helloe',23,32,23,26,634,445,26]
# d = []
# for ele in l:
#     if l.count(ele)>1 and ele not in d:
#         d.append(ele)
# print(d)

l = ['hello',23,32,32,23,54,53,55]
d = []
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and l[i] not in d:
            d.append(l[i])
print(d)
