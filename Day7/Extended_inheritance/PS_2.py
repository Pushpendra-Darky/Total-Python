class Vertebrate:
    vertebrate = True

class Bird(Vertebrate):
    has_peak = True
    def lay_eggs(self):
        print("laying eggs")

class Reptile(Vertebrate):
    poisonous = True

class Fish(Vertebrate):
    def swim(self):
        print("swimming")
    def lay_eggs(self):
        print("laying eggs")

class Mammal(Vertebrate):
    def walk(self):
        print("walking")
    def nurse(self):
        print("nursing pups")

class Platypus(Fish,Reptile,Bird,Mammal):
    pass
