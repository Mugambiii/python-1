gross_income = float(input("Enter your gross income"))
children = int(input("How many children do you have"))
dependency_exemption = 3000 * children
net_income = gross_income - dependency_exemption
print(net_income)
if net_income >=0 and net_income <=50000:
    tax = 15/100 * net_income
elif net_income >50000:
    tax = 15/100 * 50000
    print(tax)


