# Fuel required to launch modules is ((mass / 3)[rounded down] - 2)
# NEW REQUIREMENT - FUEL also needs fuel. Need to make the equation recursive? 

# fuel-input.txt is text file with masses of all modules (1 per line)


#import math
import math
# input fuel-input.txt
text_file = open("fuel-input.txt", "r")
module_masses_raw = text_file.readlines()

#module_masses = map(str.rstrip, module_masses_raw)
# strip /n and convert strings to ints
for item in module_masses_raw:
    item.rstrip()
    module_masses = [int(item) for item in module_masses_raw]
#print(module_masses)

# define function for figuring out fuel
def module_fuel_calc(mass):
    '''
        Input: mass of the module to calculate
        Returns the amount of fuel needed for this specific module
    '''
    fuel_required = math.floor(mass/3)
    fuel_required = fuel_required - 2
    total_fuel = fuel_required

    while fuel_required > 8:
        fuel_required = math.floor(fuel_required/3)
        fuel_required = fuel_required - 2
        total_fuel += fuel_required
    else:
        return total_fuel

#print(text_file)
#print(module_masses)
# initialize total-fuel variable to 0
total_fuel = 0
# for each line of fuel-input.txt
for mass in module_masses:
    # run function
    #print(total_fuel)
    # add result of each function to total-fuel
    total_fuel += module_fuel_calc(mass)
print("Total fuel needed is", total_fuel)
    