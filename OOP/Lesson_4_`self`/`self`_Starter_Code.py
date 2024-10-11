class SuperHero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
    
    def power_boost(strength_increase):
        strength += strength_increase
        print(f"{name}'s strength increased to {strength}!")

# Create a superhero
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

# Try to boost Iron Man's power
ironman.power_boost(15)