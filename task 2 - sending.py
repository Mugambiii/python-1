def sending (amount):
    balance = 5000
    if amount >=50 and amount <=500:
        balance  -=( amount - 20)
        print("New balance is {} ".format(balance))
    elif amount >= 501 and amount <=2000:
        balance -=( amount - 30)
        print("New balance is {} ".format(balance))
sending(amount=1000)
sending(amount=200)