# Define Classes
class Fish:
    '''
    Generic fish type for all vertebrate sea creatures

    Setting last_name = "Fish" since generic fish should have this last name. This will be changed for some child Classes


    '''
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish named", self.first_name, "is swimming.")

    def swim_backwards(self):
        print("The fish named", self.first_name, "is swimming in reverse.")

class Trout(Fish):
    '''
    Uses only the parent Fish class methods
    '''
    pass

class Goldfish(Fish):
    '''
    Uses only the parent Fish class methods
    '''
    pass

class Clownfish(Fish):
    '''
    This child class uses all the same attributes of the Fish parent class, but also adds a new method, live_with_anemone

    '''
    def live_with_anemone(self):
        print("The clownfish named", self.first_name, "is living in peace with the sea anemone.")

##RESUME WITH OVERRIDING PARENT METHODS: 
# https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
# Begin code
print("---====---")
#create a Trout
terry = Trout("Terry")
print(terry.first_name, terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

print("----")
#Create a Clownfish with a new method
casey = Clownfish("Casey")
print(casey.first_name, casey.last_name)
casey.swim()
casey.live_with_anemone()

print("---===---")