
# Solution

Let's have a look at the solution code:
```python
class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


quantumquake = SuperHero("Quantum Quake", "Seismic Energy Manipulation", 80)
flash = SuperHero("Flash", "Fast Movement", 90)

print(f"{quantumquake.name} has the power of {quantumquake.power} and {quantumquake.health} health.")
print(f"{flash.name} has the power of {flash.power} and {flash.health} health.")
```

Let's explain the above code to see how we solved the three tasks in our challenge:

**Task 1:** Complete the SuperHero class
- We filled in the `__init__` method. We used `self.name = name` to store the superhero's name, and did the same for power and health.

**Task 2:**: Create superhero instances
- We made two superheroes using our SuperHero class:
  1. We created Quantum Quake by writing: `quantumquake = SuperHero("Quantum Quake", "Seismic Energy Manipulation", 80)`
  2. We made Flash the same way: `flash = SuperHero("Flash", "Fast Movement", 90)`

**Task 3:**: Display superhero information
- We used `print()` to show each superhero's info.
- To get a superhero's name, we wrote `quantumquake.name`. It's like asking Quantum Quake, "What's your name?"
- We did this for the power and health too, for both superheroes.
