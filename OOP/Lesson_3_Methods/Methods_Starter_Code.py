class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
# Print the pet's hunger level after each feeding

# Print the final hunger level
print(f"{my_pet.name}'s final hunger level: {my_pet.hunger}")