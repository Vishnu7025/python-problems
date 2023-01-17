dict = {
    "key1":"value1",
    "key2":"value2"
}
dict["key3"]='valu3'
# print(dict)
# print(dict.get("key4","5"))



fruits= ['apple','grapes','banana',1,2]
fruits.append(dict)
fruits[5].update({"key4":[1,2,4,]})
# print(fruits[5].get('key4')[1])

num = [1,4,3,5,7,6,8,10,9,2,11,25]
count = len(num)


list = []
for i in range(count):
        s = min(num)
        list.append(s)
        num.remove(s)
print(list)

