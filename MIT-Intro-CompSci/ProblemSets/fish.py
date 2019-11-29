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
        print("The", self.last_name, "named", self.first_name, "is swimming.")

    def swim_backwards(self):
        print("The", self.last_name, "named", self.first_name, "is swimming in reverse.")

class Trout(Fish):
    '''
    Uses the parent class for init method, but also add a new attribute
    '''
    def __init__(self, water = "freshwater"):
        self.water = water
        # super() lets you use parent class methods even when overwriting certain aspects of these methods
        super().__init__(self)

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
        print("The", self.last_name, "named", self.first_name, "is living in peace with the sea anemone.")

class Shark(Fish):
    '''
    A child class which overrides some of the default attributes assigned to the Fish class.

    '''
    # overwriting all of the init methods in parent class
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    # overwriting the parent swim_backwards method
    def swim_backwards(self):
        print("The", self.last_name, "cannot swim backwards, but it can sink backwards.")

class Coral:
    def community(self):
        print("Coral lives in a community")

class Anemone:
    def protect_clowfish(self):
        print("The anemone is protecting the clownfish")

class CoralReef(Coral, Anemone):
    pass

##RESUME WITH Multiple Inheritance
# https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
# Begin code
print("---====---")
#create a Trout
# create the Trout object first
terry = Trout()
# THEN give it a first name, since the super() method overwrote the original init parameter
terry.first_name = "Terry"
print(terry.first_name, terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
print(terry.water)
terry.swim()
terry.swim_backwards()

print("----")
#Create a Clownfish with a new method
casey = Clownfish("Casey")
print(casey.first_name, casey.last_name)
casey.swim()
casey.live_with_anemone()

print("---")
sammy = Shark("Sammy")
print(sammy.first_name, sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.first_name, "has", sammy.skeleton, "for bones.")

print("---")
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clowfish()

print("---===---")