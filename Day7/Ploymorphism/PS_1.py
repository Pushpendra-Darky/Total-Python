# Define the objects
a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)

# Create a generator that yields the lengths of objects
def length_iterator(*objects):
    for obj in objects:
        yield len(obj)

# Iterate through the objects and display their lengths
for length in length_iterator(a_word, a_list, a_tuple):
    print(f"{length}")
'''
a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)
for obj in [a_word, a_list, a_tuple]:
    print(len(obj))
'''
