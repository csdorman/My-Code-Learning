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
    #counter for the orbit to compare with
    orbit_num = 0
    #counter for the orbit to compare against
    orbit_count = 1
    #indirect orbits for a specific index
    local_count = 0
    #indirect orbit total
    total_count = 0
    print("num",orbit_num, "count",orbit_count, "local", local_count, "total", total_count)
    for orbit_num in range(len(orbit_data)):
        for orbit in orbit_data:
            print(orbit_num, orbit)

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
