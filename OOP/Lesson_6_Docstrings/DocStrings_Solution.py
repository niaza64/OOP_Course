class Pet:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main power
        health (int): The superhero's health points
        speed (int): The superhero's speed rating
    """
    def __init__(self, name, animal_type):
        """Initialize a new Pet instance."""
        self.name = name
        self.animal_type = animal_type

    def make_sound(self):
        """Return the sound the pet makes based on its type."""
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# These lines will now print the docstrings
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)