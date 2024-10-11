class SuperHero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
    
    def power_boost(self, strength_increase):
        self.strength += strength_increase
        print(f"{self.name}'s strength increased to {self.strength}!")

# Create a superhero
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

# Boost Iron Man's power
ironman.power_boost(15)