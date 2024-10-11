## Superhero Class Challenge

In this challenge, you'll complete the implementation of a `SuperHero` class and create superhero instances.

### Tasks:

**1. Complete the `SuperHero` class:**
   - Add attributes `name`, `power`, and `health` to the `__init__` method.

**2. Create superhero instances:**
   - Instantiate at least two different superheroes using the `SuperHero` class.

**3. Display superhero information:**
   - Print out each superhero's `name`, `power`, and `health` by accessing their attributes.

### Starting Code:

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
        # TODO: Initialize the superhero's attributes here
        pass

# TODO: Create at least two Superhero instances

# TODO: Print out the attributes of each superhero
```

Note: You can remove the `pass` in the `__init__` method after adding your code.

### Hints:
- In the `__init__` method, remember to use `self` to assign the attributes. For example: `self.attribute_name = value`
- To create a hero: `hero1 = SuperHero("Hero Name", "Superpower", 100)`
- To print hero info: `print(f"{hero1.name} has the power of {hero1.power} and {hero1.health} health.")`

### Superhero Name Ideas:
You can use these names or create your own:
- Quantum Quake
- Nebula Knight
- Chrono Spark
- Zephyr
- Lumina

This challenge will help you practice initializing objects, and accessing object attributes in Python.