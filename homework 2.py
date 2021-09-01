house_allowance = 4000
car_allowance = 10000
medical = 5000
basic_salary = 70000
gross_income = house_allowance + car_allowance + medical +basic_salary
print(gross_income)
tax_due = 24/100 * gross_income
print(tax_due)
name = input("enter your name")
salutation = input("enter preffered salutation")
print("Hello {}, your gross income is {} and your due tax is {}".format(name,gross_income,tax_due))


