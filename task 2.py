# num1 = int(input("Enter number"))
# num2 = 3
# rem = num1 % num2
# if rem == 0:
#     print("{} is divisible by 3".format(num1))
# else:
#     print("{} is not divisible by 3".format(num1))


counties = ["nairobi", "meru", "kiambu", "mombasa", "kisumu"]
name = input("Give me any name of a kenyan county")
#lower function converts name to lowercase letters
if name.lower() in counties:
    print ("county name accepted")
else:
    print("County name does not exist")

#add names to an existing list
#list methods- append, insert
fruits = ["apple", "mango", "lemon"]
print(fruits)
fruit_name = input("Enter fruit name")
fruits.append(fruit_name.lower())
print(fruits)
fruit_name = input("Enter fruit name")
fruits.append(fruit_name.lower())
print(fruits)
name = "banana"
fruits.insert(1,name)
print(fruits)
name1 = "grapes"
fruits.insert(3,name1)
print(fruits)


#to remove items- use pop and remove functions
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)

#remove by item name - remove function
fruits.remove("grapes")
print(fruits)






