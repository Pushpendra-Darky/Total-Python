class Cube:

    sides = 6  # Class attribute

    def __init__(self, color):  # Instance attribute
        self.color = color

red_cube = Cube("red")
print(red_cube.color)  # Access 'color' attribute directly, no need for parentheses
