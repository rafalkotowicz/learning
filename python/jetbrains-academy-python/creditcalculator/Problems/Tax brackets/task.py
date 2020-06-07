def tax_bracket(taxable_income):
    if taxable_income <= 15527:
        return 0
    elif 15528 <= taxable_income <= 42707:
        return 15
    elif 42708 <= taxable_income <= 132406:
        return 25
    elif taxable_income >= 132406:
        return 28


income = int(input())
percent = tax_bracket(income)
calculated_tax = income * percent / 100
print(f"The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!")
