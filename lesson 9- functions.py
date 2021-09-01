def add(num1,num2,num3):
    result = num1 + num2 + num3
    return result
# add(num1 = 10, num2 = 30, num3 = 45)
# add(10,30,45)
# result = add (10,30,45)
# print(result)


def display_customers(customers):
    return(customers)
my_customers= display_customers(["Babra","John","Kevin"])
print (my_customers)
for customer in my_customers:
    print ("Hello {}.".format(customer))
    