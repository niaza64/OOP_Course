class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
    
    def feed(self):
        self.hunger -= 1
        print(f"{self.name} has been fed.")

# Create a pet
my_pet = Pet("Fluffy")

# Feed the pet three times
for i in range(3):
    my_pet.feed()
    print(f"{my_pet.name}'s hunger level: {my_pet.hunger}")

# Print the final hunger level
print(f"{my_pet.name}'s final hunger level: {my_pet.hunger}")