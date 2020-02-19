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
    orbit_num = 0
    orbit_compare = 1
    #while orbit_compare < len(orbit_data):
    for orbit in orbit_data: 
        while orbit_compare < len(orbit_data):
            if orbit[-1] == orbit_data[orbit_compare][0]:
                print(orbit_num, orbit_compare, len(orbit_data))
                indirect_orbits += 1
                orbit_compare += 1
            else:
                orbit_compare += 1
        orbit_num += 1
    return indirect_orbits

#print orbit data
print(orbit_data)
print(direct_orbit_count(orbit_data))
print(indirect_orbit_count(orbit_data))
