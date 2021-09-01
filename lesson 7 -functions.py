def addition():
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    result = num1 + num2
    print("{} + {} ={}".format(num1, num2, result))
#addition

# def addition2(num1,num2,num3):
#     result = num1 + num2 + num3
#     print("{} + {} ={}".format(num1, num2,num3, result))
# addition2(num1 = 10, num2 = 30, num3 = 50)

# def welcome (name):
#     print("Welcome {}".format(name))
# welcome(name="Babra")
# welcome(name = "Jackson")

# def student_marks(name,marks):
    # print(name)
    # print(marks)
#     total_marks = 0
#     for score in marks:
#         total_marks += score
#     print("Hi {} . Your total marks is {}".format(name,total_marks))
#
# student_marks(name = "Babra", marks = [70,87,90])
# student_marks(name = "John",marks = [76,67,86])

#list of customers
#print "Happy to serve you XX for every customer

# def customer_list(customers):
#     for name in customers:
#         print("Happy to serve you {}".format(name))
#
# customer_list(customers=["Babra","John","Kevin"])

def withdraw(amount):
    balance = 1000
    if amount <50:
        print("amount less than allowed minimum")
    elif amount >= 70000:
        print("amount exceeds the maximum limit")
        print("withdraw not possible")
    elif amount > balance:
        print("insufficient funds")
        print("withdraw not possible")
    else:
        balance -= amount
        print("withdraw transaction of {} successful. New balance is {}".format(amount,balance))
withdraw(amount = 999)










