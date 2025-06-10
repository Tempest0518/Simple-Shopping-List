shopping_list = []

while True:
    list = input("Enter the items into the shopping list (press q to end): ")
    if list.lower() == "q":
        break
    else:
        shopping_list.append(list)

while True:
    sort = input("Would you like the list sorted in a-z format? (Y/N) ")
    if sort.capitalize() == "Y":
        shopping_list.sort()
        break
    else:
        break

for items in shopping_list:
    print(items, end=" ")
    print()
