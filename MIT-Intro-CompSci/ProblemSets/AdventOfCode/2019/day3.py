
# Using "taxicab geometry" (grid): https://en.wikipedia.org/wiki/Taxicab_geometry
# Reddit hints for day 3: https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/
# Walkthrough (in php) is here for thought process: https://hwright.com/advent-of-code-hints-2019

# test 1
# wire 1: R8,U5,L5,D3
# wire 2: U7,R6,D4,L4
# distance from crossing to start: 3 + 3 = 6

# test 2
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83
# distance: 159

# test 3
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
# distance: 135


import sys

def calc_step_points(path):
    # set everything to 0
    curx = cury = step = 0
    #give direction dict
    directions = {'R': (1,0), 'L': (-1,0), 'U':(0,1), 'D': (0,-1)}
    points = {}
    for segment in path:
        # segment is individual direction (R8 or D3, etc)
        # look at segment char 0 and look up the direction in 'directions' dict
        # this uses a dict to connect the given letter (U) to the action ((0,1). Neat)
        dx, dy = directions[segment[0]]
        for _ in range(int(segment[1:])):
            # depending on whether the dict looks up an action using the x (L,R) or y (U,D) axis
            # use either dx or dy and assign to correct 'cur' variable
            curx += dx
            cury += dy
            # use steps to track the number of steps the wire takes
            step += 1
            if (curx, cury) not in points:
                points[(curx, cury)] = step
    return points

wire1_path, wire2_path = open('wire-grid.txt').read().split()
wire1_path, wire2_path = wire1_path.split(','), wire2_path.split(',')

wire1_points = calc_step_points(wire1_path)
wire2_points = calc_step_points(wire2_path)
intersection_points = [point for point in wire1_points if point in wire2_points]

#print(wire1_points, wire2_points)
#print(intersection_points)

part1 = min(abs(x) + abs(y) for (x, y) in intersection_points)
print("Part 1 answer is:", part1)
