#load orbit data
raw_data = open("test-data6.txt", "r")
raw_data = raw_data.read()
orbit_data = raw_data.splitlines()

# direct_orbit_count not needed. Function duplicated in indirect_orbit_count
def direct_orbit_count(orbit_data):
    direct_orbits = 0
    for orbit in orbit_data:
        direct_orbits += 1
    return direct_orbits

def find_orbit_sep(orbit1, orbit2):
    orbit_loc1 = orbit1.find(')')
    orbit_loc2 = orbit2.find(')')
    return orbit_loc1, orbit_loc2

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
    #print(counter, current_item)
    #initial comparison
    while counter > 0:
        #find location of ')' orbit separator
        orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[counter], orbit_data[prev_counter])
        if orbit_data[counter][:orbit_loc] == orbit_data[prev_counter][orbit_loc_prev+1:]:
            indirect_orbits += 1
            orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[current_item], orbit_data[prev_item])
            if orbit_data[current_item][:orbit_loc] == orbit_data[prev_item][orbit_loc_prev+1:]:
                #git print(current_item, prev_item)
                indirect_orbits += 1
                current_item -= 1
                prev_item = current_item - 1
            else:
                current_item -= 1
                prev_item = current_item - 1
            print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
        else:
            orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[current_item], orbit_data[prev_item])
            while prev_item > -1:
                if orbit_data[current_item][:orbit_loc] == orbit_data[prev_item][orbit_loc_prev+1:]:
                        indirect_orbits += 1
                        current_item -= 1
                        prev_item = current_item - 1 
                else:
                    current_item -= 1
                    prev_item = current_item - 1
            print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
        print(orbit_data[counter][:orbit_loc], orbit_data[prev_counter][orbit_loc_prev+1:])
        counter -= 1
        prev_counter = counter - 1
        current_item = counter - 1
        prev_item = current_item - 1
    return(indirect_orbits)

#print orbit data
#print(direct_orbit_count(orbit_data)) #not needed now
print(indirect_orbit_count(orbit_data))
