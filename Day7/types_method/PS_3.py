class Character:
    def __init__(self, arrows_amount):
        self.arrows_amount = arrows_amount

    def throw_arrow(self):
        if self.arrows_amount > 0:
            self.arrows_amount -= 1
        else:
            print("No more arrows left!")

# Create a Character instance with an initial number of arrows
character = Character(10)

# Call throw_arrow() method to throw an arrow
character.throw_arrow()

# Check the updated arrows_amount
print("Remaining arrows:", character.arrows_amount)
