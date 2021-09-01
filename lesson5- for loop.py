#For loop - repetition of tasks
#iterating through a sequece of characters
#or range of numbers and do something
for number in range(0,10):
    print(number)

for number in range(10,20):
    print(number)

name = "Welcome"
for letter in name:
    print(letter)

print(name[0])

statement = "Welcome Babra."
for character in statement:
    print(character)

for count in range (3):
    print(count)

for attempts in range (3):
    password = input("Enter your password")
    if password == "creative":
        print("correct password")
        #break loop
        break
    else:
        print("incorrect password")
        continue




