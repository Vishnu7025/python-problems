original_list = [1, 2, 3, 3, 4, 4, 5, 5, 6]
new_list = []
for x in original_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)
