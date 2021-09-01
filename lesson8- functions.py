def greater_number (x,y):
    if x>y:
        print("{} is greater than {}".format(x,y))
    elif x==y:
        print("{} is equivalent to {}".format(x,y))
    else:
        print("{} is less than {}".format(x,y))
# greater_number(20,40)
# greater_number(4,16)
# greater_number(60,12)

def my_name(name):
    return name
# my_name(name = "Babra")
returned_name = my_name(name = "Babra")
print(returned_name)
print("Hello",returned_name)

#4+6*2+50/4 - BODMAS
def my_age(age = 18):
    return age
print (my_age())

def addition(num1,num2):
    return num1 + num2
ans = addition(4,5)

def division (x,y):
    return x/y
ans1 = division(50,4)

def multiply(x,y):
    return x*y
ans2 = multiply(6,2)

4+ ans2 + ans1
final_ans1 = addition(4,ans2)
final = addition(final_ans1,ans1)
print("final ans",final)
print(4 + 6 *2 + 50/4)
result = division(addition(20,30), addition(200,300))
print(result)

def check_balance():
    balance = 1000
    return balance

def deposit():
    amount= float(input("Enter deposit amount"))
    my_balance = check_balance()
    my_balance += amount
    statement = "Deposit of kes {} is successful. New balance is {}".format(amount,my_balance)
    return statement
msg = deposit()
print (msg)







