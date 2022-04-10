grocery_list = ["Bread", "Tomato", "Onion"]
grocery_list.append("Milk")
count = 0
for i in grocery_list:
    count+=1
    print(i)
    if (i=="Bread"): print ("Not gluten free")
print("There are ", count, " items")
grocery_list.remove("Bread")