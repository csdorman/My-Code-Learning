#load orbit data
raw_data = open("test-data6.txt", "r")
raw_data = raw_data.read()
orbit_data = raw_data.splitlines()


def direct_orbit_count(orbit_data):
    direct_orbits = 0
    for orbit in orbit_data:
        direct_orbits += 1
    return direct_orbits

def indirect_orbit_count_2(orbit_data):
   #NEED TO START AT BACK OF ORBIT DATA
    #current index item
    current_item = len(orbit_data)-2
    #previous index item
    prev_item = current_item - 1
    #keep track of WHERE TO START 
    counter = len(orbit_data)-1
    prev_counter = counter - 1
    #indirect orbits
    indirect_orbits = 0
    print("Item#", current_item, "Prev#",prev_item)
    #initial comparison
    while counter > 0:
        if orbit_data[counter][0] == orbit_data[prev_counter][-1]:
            indirect_orbits += 1
            while prev_item > -1:
                if orbit_data[current_item][0] == orbit_data[prev_item][-1]:
                    indirect_orbits += 1
                    current_item -= 1
                    prev_item -= 1
                else:
                    current_item -= 1
                    prev_item -= 1
            counter -= 1
        else:
            while prev_item > -1:
                if orbit_data[current_item][0] == orbit_data[prev_item][-1]:
                        indirect_orbits += 1
                        current_item -= 1
                        prev_item -= 1
                else:
                    current_item -= 1
                    prev_item -= 1
            counter -= 1
    return(indirect_orbits)

def indirect_orbit_count(orbit_data):
    local_indirect = 0
    total_indirect = 0
    #index to compare with
    orbit_num = 0
    orbit_compare = 1
    #while orbit_compare < len(orbit_data):
    print("orbit",orbit_num, orbit_compare)
    print("orbit data len", len(orbit_data))
    for orbit_num in range(len(orbit_data)):
    #while orbit_compare < len(orbit_data):
        for orbit in orbit_data:
            print(orbit)
            if orbit[-1] == orbit_data[orbit_compare][0]:
                local_indirect += 1
                print("orbits",local_indirect, total_indirect)
                print("pass",orbit_compare)
                orbit_compare += 1
            else:
                orbit_compare += 1
                total_indirect = local_indirect
                print("fail", orbit_compare)
        orbit_num += 1
    return (total_indirect)

    #There are 11 direct and 31 indirect orbits in the test
    #for a total of 42 orbits

    #NEED TO REDO WITH RECURSION(?) MATH IS WRONG
    #compare orbit[0][-1] with orbit[1][0]
        #if match 
            # add +1 to local indirect orbits
            # compare orbit[1][-1] with orbit[2][0]
                #continue this way until no match
        #if no match
            # save local indirect to total indirect
            # compare orbit[0][-1] to orbit[x][0]


#print orbit data
print(orbit_data)
print(direct_orbit_count(orbit_data))
print(indirect_orbit_count_2(orbit_data))
