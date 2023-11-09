class Wizard:
    def defend(self):
        print("magic shield")

class Archer:
    def defend(self):
        print("duck")

class Samurai:
    def defend(self):
        print("block")

def general_defense(character):
    if hasattr(character, 'defend') and callable(getattr(character, 'defend')):
        character.defend()
    else:
        print("This character cannot defend.")

# Create instances of character classes
wizard = Wizard()
archer = Archer()
samurai = Samurai()

# Call the general_defense function with different character instances
general_defense(wizard)  # Calls the defend() method of Wizard
general_defense(archer)  # Calls the defend() method of Archer
general_defense(samurai)  # Calls the defend() method of Samurai

# Call the general_defense function with an object that cannot defend
general_defense("InvalidCharacter")  # Prints "This character cannot defend."


'''
class Wizard():
    def defend(self):
        print("magic shield")
class Archer():
    def defend(self):
        print("duck")
class Samurai():
    def defend(self):
        print("block")
def general_defense(character):
    character.defend()
'''
