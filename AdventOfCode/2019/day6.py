#load orbit data
raw_data = open("data6.txt", "r")
raw_data = raw_data.read()
orbit_data = raw_data.splitlines()

# direct_orbit_count not needed. Function duplicated in indirect_orbit_count
def direct_orbit_count(orbit_data):
    direct_orbits = 0
    for orbit in orbit_data:
        direct_orbits += 1
    return direct_orbits

def indirect_orbit_count(orbit_data):
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
    #initial comparison
    while counter > 0:
        #print(orbit_data[counter][:3], orbit_data[prev_counter][-3:])
        if orbit_data[counter][:3] == orbit_data[prev_counter][-3:]:
            indirect_orbits += 1
            while prev_item > -1:
                if orbit_data[current_item][:3] == orbit_data[prev_item][-3:]:
                    print(current_item, prev_item)
                    indirect_orbits += 1
                    current_item -= 1
                    prev_item = current_item - 1
                else:
                    current_item -= 1
                    prev_item = current_item - 1
        else:
            while prev_item > -1:
                if orbit_data[current_item][:3] == orbit_data[prev_item][-3:]:
                        indirect_orbits += 1
                        current_item -= 1
                        prev_item = current_item - 1 
                else:
                    current_item -= 1
                    prev_item = current_item - 1
        counter -= 1
        prev_counter = counter - 1
        current_item = counter - 1
        prev_item = current_item - 1
    return(indirect_orbits)



#print orbit data
print(indirect_orbit_count(orbit_data))
