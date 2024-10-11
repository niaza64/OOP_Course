class Pet:
    def __init__(self, name, species, hunger, energy):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

# Create a pet named Whiskers
whiskers = Pet("Whiskers", "cat", 6, 8)

# Print Whiskers' initial attributes
print("Initial Attributes:")
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# Modify Whiskers' attributes
whiskers.hunger -= 3
whiskers.energy += 2

# Print Whiskers' modified attributes
print("\nModified Attributes:")
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")