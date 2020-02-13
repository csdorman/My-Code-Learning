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
    indirect_orbits = 0
    for orbit in orbit_data:
        orbit_num = 0
        #if 3rd char of orbit x == 1st char of orbit x+1
        if orbit_data[orbit_num][2] == orbit_data[orbit_num + 1][0]:
            indirect_orbits += 1
            orbit_num += 1
        else:
            orbit_num += 1
    return indirect_orbits

#print orbit data
print(orbit_data)
print(direct_orbit_count(orbit_data))
print(indirect_orbit_count(orbit_data))
