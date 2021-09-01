def deposit():
    amount= float(input("Enter deposit amount"))
    my_balance = check_balance()
    my_balance += amount
    statement = "Deposit of kes {} is successful. New balance is {}".format(amount,my_balance)
    return statement
msg = deposit()
print (msg)





