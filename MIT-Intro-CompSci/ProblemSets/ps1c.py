# ask for total house cost
house_cost = float(input("How much does the house cost?"))
# ask for starting salary
annual_salary = float(input("What is your annual salary?"))
monthly_salary = annual_salary / 12

# set initial variables
# annual raise percentage
semi_annual_raise = 0.07
# annual investment return
investment_return = 0.04
# down payment amount
down_payment = house_cost * 0.25
savings_amount = 0

# bisection search to find optimum savings rate
target = 36
num_guesses = 0
epsilon = 100
low = 0
high = 10000
guess = (high + low)/ 2



