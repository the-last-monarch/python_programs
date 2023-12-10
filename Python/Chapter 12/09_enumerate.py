list1 = [3, 4.3, True, "Shadow", 43]

# long method
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

# enumerate method
for index, item in enumerate(list1):
    print(item, index)