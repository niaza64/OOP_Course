# Superhero Abilities Challenge

In this challenge, you'll extend the SuperHero class by adding new ability methods. The class and its attributes have already been defined in the provided code. Your tasks are outlined below:

## Tasks:

**1. Enhance the `SuperHero` class:**
   - Add methods `attack()` and `heal()` to the `SuperHero` class.

**2. Implement the ability methods:**
   - `attack()`: Should print a message about the superhero attacking by accessing the superhero `power` attribute.
   - `heal()`: Should increase the superhero's `health` attribute by 10 points and print message about the new health.

**3. Create superhero instances:**
   - Create two different superheroes using the `SuperHero` class.

**4. Use the abilities:**
   - Call the `attack()` and `heal()` methods for each superhero.


## Starting Code:

```python
class SuperHero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
    

      # TODO: Define attack method and implement it

      # TODO: Define heal method and implment it
     

# TODO: Create two superhero instances

# TODO: Use the attack() and heal() methods for each superhero
```

## Hints:
- Remember, when defining methods in a class, always include `self` as the first parameter. For example: `def method_name(self):`.
- In the `attack()` method, use `print()` to show a message like "[name] attacks with [power]!"
- For `heal()`, increase `self.health` by 10 and print a message about healing.
- To create a hero: `hero1 = SuperHero("Hero Name", "Superpower", 100)`
- Remember to remove `pass` when you add code to a method.

## Example Superheroes:
- Spider-Man (power: web-slinging and wall-crawling, health: 100)
- Wonder Woman (power: super strength and lasso of truth, health: 110)
- Iron Man (power: high-tech armor, health: 95)

This challenge will help you practice creating methods, working with object attributes.