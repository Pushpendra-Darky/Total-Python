class Wizard:
    def attack(self):
        print("magic attack")

class Archer:
    def attack(self):
        print("shoot arrow")

class Samurai:
    def attack(self):
        print("katana attack")

# Instantiate characters
archer = Archer()
wizard = Wizard()
samurai = Samurai()

# Build an iterable list of characters
characters = [archer, wizard, samurai]

# Create an iterator that performs the conjugate attack
class ConjugateAttackIterator:
    def __init__(self, characters):
        self.characters = characters
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.characters):
            raise StopIteration
        character = self.characters[self.index]
        self.index += 1
        return character.attack()

# Iterate through characters and perform the conjugate attack
conjugate_attack_iterator = ConjugateAttackIterator(characters)
for _ in conjugate_attack_iterator:
    pass  # Attack methods will be called in the desired order

'''

class Wizard():
    def attack(self):
        print("magic attack")
class Archer():
    def attack(self):
        print("shoot arrow")
class Samurai():
    def attack(self):
        print("katana attack")
gandalf = Wizard()
hawkeye = Archer()
jack = Samurai()
characters = [hawkeye, gandalf, jack]
for char in characters:
    char.attack()

'''
