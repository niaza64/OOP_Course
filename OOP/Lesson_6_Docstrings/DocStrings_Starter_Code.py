class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def make_sound(self):
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"


# These lines will print None until you add docstrings
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)