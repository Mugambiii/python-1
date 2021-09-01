def deposit(amount):
    balance = 5000
    if amount <100:
        print("Amount is less than allowed minimum")
    elif amount >= 50000:
        print("Error.Amount is more than allowed maximum")
    else:
        balance += amount
        print("Deposit transaction of {} successful. You have a current balance of {} in your account".format(amount,balance))
deposit(amount=70)
