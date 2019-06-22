# ask for total house cost
house_cost = 1000000
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
target = 36 #number of months
steps = 0
epsilon = 100 
low = 0 #0% savings rate
high = 10000 #100% savings rate
guess = (high + low)/ 2 #bisection search -> start at 50%
savings_amount = 0
semi_annual_raise = 0.07
annual_salary_raised = annual_salary
while savings_amount <= (down_payment - epsilon):
    for month in range(target): 
        savings_amount = savings_amount + (monthly_salary * (guess/100))
        if month % 6 == 0:
            annual_salary_raised = annual_salary_raised + (annual_salary_raised * semi_annual_raise)
            monthly_salary = annual_salary_raised / 12
    if savings_amount >= (down_payment + epsilon) and target == 36:
        high = guess
        guess = (high + low) /2
        print("Savings too great.")
        print("Guess = " + str(guess))
        savings_amount = 0
        semi_annual_raise = 0.07
        annual_salary_raised = annual_salary
        steps == steps + 1
    elif savings_amount <= (down_payment - epsilon) and target == 36:
        low = guess
        guess = (high + low) /2
        print("Savings too little. Break")
        savings_amount = 0
        semi_annual_raise = 0.07
        annual_salary_raised = annual_salary
        steps == steps + 1
    else:
        print("Your starting salary is " + str(annual_salary))
        print("Your best savings rate is " + str((guess * .01)))
        print("It took me " + str(steps) + " tries to find this answer")
    

#Got loop working (kind of), but it's not outputting the correct answer yet.
       

#pseudo code - looking to find the best savings rate to save down payment (within 100) in 36 months
#for loop run 36 times
#pick savings percentage
#every month, add monthly savings percentage to savings account
#check if savings amount within down payment epsilon
#if it takes fewer than 36 months, shrink savings percent
#if it takes more than 36 months, increase savings percent

        

# find the BEST SAVINGS RATE to get to DOWN PAYMENT amount
# Savings should be within 100 of down payment amount (not exact amount)




