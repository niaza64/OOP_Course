class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

# Test your class
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")