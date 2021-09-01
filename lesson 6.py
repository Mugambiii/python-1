# running = True
# while running:
#     print("program is running")

# # it requires starting point, steps and an end.
# count = 0
# while count <=10:
#     print(count)
#     count += 2
#
# #word guess
count = 0
while count <3 :
    word_list = ["python", "css","html","coding"]
    word = input("Guess a word")
    if word in word_list:
        print("Correct guess")
    else:
        print("Wrong guess. Try again")
    count += 1

#logical adding - and
#logical oring - or
#two monkeys smiling

monkey_a_smiling = False
monkey_b_smiling = False
if monkey_b_smiling and monkey_a_smiling:
    print("There is trouble")
elif monkey_b_smiling or monkey_a_smiling:
    print("We are safe")
elif not monkey_a_smiling and not monkey_b_smiling:
    print("Be careful.")



















