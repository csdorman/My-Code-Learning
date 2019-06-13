# current savings
current_savings = 0

# annual rate of return
r = 0.04

# find yearly (and monthly) salary
annual_salary = float(input("What is your annual salary?"))
monthly_salary = annual_salary / 12

# find savings rate
portion_saved = float(input("What percent (as a decimal) of your salary will you save each month?"))

#find out the house price
total_cost = float(input("How much does the house cost?"))

# figure out down payment and return
portion_down_payment = total_cost * 0.25
print("Your down payment will be $" + str(portion_down_payment))

monthly_savings = monthly_salary / portion_saved

if portion_saved >= portion_down_payment:
    month_counter = 0
    # add savings amount to current savings
    current_savings = current_savings + monthly_savings
    # add investment income to current savings
    current_savings = current_savings + (current_savings * (r/12))
    month_counter = month_counter + 1
    print("Number of months: " + str(month_counter))
