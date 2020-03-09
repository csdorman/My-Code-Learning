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

def find_orbit_sep(orbit1, orbit2):
    orbit_loc1 = orbit1.find(')')
    orbit_loc2 = orbit2.find(')')
    return orbit_loc1, orbit_loc2

def orbit_count(orbit_data):
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
    while counter > -1:
        #find location of ')' orbit separator
        orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[counter], orbit_data[prev_counter])
        #check if counter and prev_counter match
        if orbit_data[counter][:orbit_loc] == orbit_data[prev_counter][orbit_loc_prev+1:]:
            #if the DO match add 1 to indirect orbit
            indirect_orbits += 1
            #iterate through all the list items under a specific counter
            while prev_item > -1: #Do I need to also make current_item index a part of this?
                #find location of orbit separator
                #check if current_item and prev_item match
                #print("Before IF")
                #print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
                #print(orbit_loc, orbit_loc_prev)
                if orbit_data[current_item][:orbit_loc] == orbit_data[prev_item][orbit_loc_prev+1:]:
                    #git print(current_item, prev_item)
                    #if they do match
                    indirect_orbits += 1
                    #step back for previous item
                    prev_item -= 1
                    if current_item != prev_item + 1:
                        current_item = prev_item +1
                else:
                    #current_item -= 1
                    #move prev_item backwards through the list
                    prev_item -= 1
                orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[current_item], orbit_data[prev_item])
                #print("After IF")
                #print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
                #print(orbit_loc, orbit_loc_prev)
            #print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
        else:
            while prev_item > -1:
                if orbit_data[current_item][:orbit_loc] == orbit_data[prev_item][orbit_loc_prev+1:]:
                    indirect_orbits += 1
                    prev_item -= 1
                    if current_item != prev_item + 1:
                        current_item = prev_item +1
                else:
                    prev_item -=1
                    #current_item -= 1
                    #prev_item = current_item - 1
                orbit_loc, orbit_loc_prev = find_orbit_sep(orbit_data[current_item], orbit_data[prev_item])
            #print(orbit_data[current_item][:orbit_loc], orbit_data[prev_item][orbit_loc_prev+1:])
        print(counter + 1, prev_item, indirect_orbits)
        #print(orbit_data[current_item], orbit_data[prev_item])
        #print(orbit_data[counter][:orbit_loc], orbit_data[prev_counter][orbit_loc_prev+1:])
        counter -= 1
        prev_counter = counter - 1
        current_item = counter - 1
        prev_item = current_item - 1
    print("Direct",len(orbit_data))
    print("Indirect",indirect_orbits)
    indirect_orbits += len(orbit_data)
    return(indirect_orbits)

#print orbit data
#print(direct_orbit_count(orbit_data)) #not needed now
print(orbit_count(orbit_data))
