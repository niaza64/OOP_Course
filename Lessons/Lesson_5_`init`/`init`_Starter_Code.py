class Pet:
    name = ""
    species = ""
    age = 0
    
    # TODO: Implement the __init__ method here

# Don't modify the code below this line
# Create pets
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

# Display pet information
print(f"{fluffy.name} is a {fluffy.age}-year-old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age}-year-old {buddy.species}.")