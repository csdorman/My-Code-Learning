#load orbit data
raw_data = open("test-data6.txt", "r")
raw_data = raw_data.read()
orbit_data = raw_data.splitlines()


def direct_orbit_count(orbit_data):
    direct_orbits = 0
    for orbit in orbit_data:
        direct_orbits += 1
    return direct_orbits

def indirect_orbit_count(orbit_data):
    local_indirect = 0
    total_indirect = 0
    #index to compare with
    orbit_num = 0
    orbit_compare = 1
    while orbit_num < len(orbit_data):
        print(orbit_num)
        for orbit in orbit_data:
            if orbit_data[orbit_compare-1][-1] == orbit_data[orbit_compare][0]:
                local_indirect += 1
                orbit_compare += 1
            else:
                total_indirect = local_indirect
        orbit_num += 1
    return (total_indirect)


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
print(indirect_orbit_count(orbit_data))
