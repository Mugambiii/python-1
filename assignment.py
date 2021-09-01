count = 0
correct_count=0
wrong_count=0
while count <3 :
    word_list = ["python", "css","html","coding"]
    word = input("Guess a word")
    if word in word_list:
        print("Correct guess")
        correct_count +=1
    else:
        print("Wrong guess. Try again")
        wrong_count +=1
    count += 1
print("you got {} correct guesses".format(correct_count))
print("you got {} wrong guesses".format(wrong_count))


    




