# Write a program that replaces these letters with something a bit more human-readable, and calculate the interest for
# some varying amounts of money at realistic interest rates such as 1%, and -0.05%.
initial_investment_str = input("What was your initial investment?")
pay_out_frequency_str = input("How often is the interest paid out per year?")
interest_rate_str = input("What is the interest rate p.a.?")
years_str = input("For how many years is the money invested?")

initial_investment = int(initial_investment_str)
pay_out_frequency = int(pay_out_frequency_str)
interest_rate = int(interest_rate_str)
years = int(years_str)

final_amount = initial_investment * (1 + (interest_rate/100)/years)**(pay_out_frequency*years)
print("your final amount is", final_amount, "€")
# When you have that working, # ask the user for the value of some of these variables and do the calculation.