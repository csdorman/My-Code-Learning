
# Using "taxicab geometry" (grid): https://en.wikipedia.org/wiki/Taxicab_geometry
# Reddit hints for day 3: https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/
# Walkthrough (in php) is here for thought process: https://hwright.com/advent-of-code-hints-2019

def read_file():
    '''
    Opens the wire-grid.txt file
    '''
    # Import wire-grid.txt file
    # Split at /n 
    # Save wires separately
    wire1_directions = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    wire2_directions = ["U62","R66","U55","R34","D71","R55","D58","R83"]

def wire_tracking():
    # Set wire 1 x and y to 0
    wire1_axis = [0,0]
    # Set wire 2 x and y to 0
    wire2_axis = [0,0]
    # For directions with "U" or "D", modify y axis
    # If "U" y = +num
    # If "D" y = -num
    # For directions with "L" or "R", modify x axis
    # If "R" x = +num
    # If "L" x = -num

read_file()
wire_tracking()

