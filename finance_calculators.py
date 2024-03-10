import math

#user picks investment or bond
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

choice = choice.lower()

#error message if neither investment nor bond
if choice != "investment" and choice != "bond":
    print("That is an invalid choice. Please relaunch the programme to continue.")

#investment calculator
elif choice == "investment":
   
    print("You have chosen the investment calculator.")

    deposit_amount = float(input("What is your deposit amount? Please enter without £."))
    interest_rate = float(input("What is your interest rate? Please enter without %."))
    years_invested = int(input("For how many years do you plan on investing?"))
    interest = input("And is this simple or compound interest?")
    interest = interest.lower()

    print("Calculating your return on investment...")

    interest_rate = interest_rate / 100

    if interest == "simple":
        simple_investment_return = deposit_amount * (1 + interest_rate*years_invested)
        print(f"Your return on investment is £{simple_investment_return:.2f}.")
    elif interest == "compound":
        compound_investment_return = deposit_amount * math.pow((1+interest_rate), years_invested)
        print(f"Your return on investment is £{compound_investment_return:.2f}.")
    else:
        print("That is an invalid type of interest. Please pick 'simple' or 'compound'.")

#bond calculator
elif choice == "bond":

    
    print("You have chosen the bond calculator.")

    house_value = float(input("Please share the present value of the house (without £):"))
    interest_rate = float(input("Please input the interest rate (excluding a % mark):"))
    months_to_repay = int(input("Please input the number of months you plan to repay the bond:"))

    print("Calculating your monthly repayment amount...")

    interest_rate = interest_rate / 100
    interest_rate = interest_rate / 12

    monthly_repayment_amount = (interest_rate * house_value) / (1 - (1 + interest_rate)**(-months_to_repay))

    print(f"Your monthly repayment amount is £{monthly_repayment_amount:.2f}.")

