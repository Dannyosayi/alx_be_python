Monthly_income = int(input("Enter your monthly income: "))
Monthly_expenses = int(input("Enter your total monthly expenses:"))

Monthly_savings = Monthly_income - Monthly_expenses
Interest = 0.05
Projected_savings = Monthly_savings * 12 + ((Monthly_savings * 12 * Interest))

print(Monthly_expenses)
print(Monthly_income)
print(Monthly_savings)
print(" Projected savings after one year, with interest, is :", Projected_savings)