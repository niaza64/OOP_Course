# Solution: Super Hero Abilities

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
    
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")
    
    def heal(self):
        self.health += 10
        print(f"{self.name} healed. New health: {self.health}")

# Create two superhero instances
spiderman = SuperHero("Spider-Man", "web-slinging and wall-crawling", 100)
wonderwoman = SuperHero("Wonder Woman", "super strength and lasso of truth", 110)

# Use the attack() and heal() methods for each superhero
spiderman.attack() # Spider-Man attacks with web-slinging and wall-crawling!
spiderman.heal() # Spider-Man healed. New health: 110

wonderwoman.attack() # Wonder Woman attacks with super strength and lasso of truth!
wonderwoman.heal() # Wonder Woman healed. New health: 120 
```

Let's explain the above code to see how we solved the four tasks in our challenge:

**Task 1:** Enhance the SuperHero class
- We added two new methods to the `SuperHero` class: `attack()` and `heal()`.

**Task 2:** Implement the ability methods
- In the `attack()` method, we used `print()` to show a message about the superhero attacking with their power.
- In the `heal()` method, we increased the superhero's health by 10 points using `self.health += 10`, and then printed a message about the new health.

**Task 3:** Create superhero instances
- We created two superheroes using our SuperHero class:
  - We created Spider-Man by writing: `spiderman = SuperHero("Spider-Man", "web-slinging and wall-crawling", 100)`
  - We created Wonder Woman the same way: `wonderwoman = SuperHero("Wonder Woman", "super strength and lasso of truth", 110)`

**Task 4:** Use the abilities
- We called the `attack()` and `heal()` methods for each superhero:
  - For Spider-Man: `spiderman.attack()` and `spiderman.heal()`
  - For Wonder Woman: `wonderwoman.attack()` and `wonderwoman.heal()`