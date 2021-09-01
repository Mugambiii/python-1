# def withdraw():
#     balance = 2000
#     withdraw = float(input("Enter amount you wish to withdraw"))
#     new_balance = balance - withdraw
#     statement = ("Withdraw of kes {} successful. Balance is {}".format(withdraw,new_balance))
#     return statement
# msg = withdraw
# print(msg)



def withdraw(amount):
    balance = 2000

    new_balance = balance - amount
    statement = ("Withdraw of kes {} successful. Balance is {}".format(amount,new_balance))
    return statement
msg = withdraw(amount=4000)
msg = withdraw(amount=500)
print(msg)



