# Lesson 3: Giving Superheroes Superpowers with Methods

In this lesson, we'll cover:
- What are methods and why we need them
- How to define methods in a class
- Creating two action methods for our superheroes
- Calling methods on our superhero objects
- Hands-on challenge: Implement and use a method to feed a pet

## What are methods and why do we need them?

You may be wondering, **Our superheroes aren't very super yet. They have characteristics, but they're not actually doing anything!** And you'd be absolutely right. A superhero who can't use their powers isn't much of a hero at all. This is where methods come in.

*Methods are functions that belong to a class. They define the behaviors and actions that objects of the class can perform.*

In our superhero context, methods will allow our heroes to actually use their powers and interact with the world around them!

## Defining methods in a class

Let's update our `SuperHero` class to include two methods:

```python
class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")
```

Let's break down what's happening in this code:

1. We've added two new methods to our `SuperHero` class: `use_power()` and `take_damage()`.

2. The `use_power()` method:
   - Takes no parameters (except `self`, which we'll explain in a future lesson).
   - Prints a message saying the superhero is using their power.

3. The `take_damage(amount)` method:
   - Takes a parameter `amount`, which represents how much damage the superhero is taking.
   - Subtracts this amount from the superhero's health.
   - Prints a message about the damage taken and the superhero's new health.

### Methods: Functions Inside a Class

At their core, methods are simply functions that are defined inside a class. They allow objects of that class to perform actions or behaviors.

## Calling methods on our superhero object

Now that we have methods, let's create a superhero and make them use their powers or iteract with the world!

```python
# Create a superhero
spiderman = SuperHero("Spider-Man", "web-slinging", 100, 80)

# Use the superhero's power
spiderman.use_power()
# Output: Spider-Man uses web-slinging!

# Make the superhero take some damage
spiderman.take_damage(20)
# Output: Spider-Man takes 20 damage. Health is now 80.

# Use the power again
spiderman.use_power()
# Output: Spider-Man uses web-slinging!

# Take more damage
spiderman.take_damage(50)
# Output: Spider-Man takes 50 damage. Health is now 30.
```

In this example, we:
1. Created a `SuperHero` object named `spiderman`.
2. Called the `use_power()` method on `spiderman`.
3. Called the `take_damage()` method on `spiderman`, passing 20 as the amount of damage.
4. Called `use_power()` again to show that Spider-Man can still use his power after taking damage.
5. Called `take_damage()` again with a different amount of damage.

Each time we call a method, it performs the action we defined in the class, using the specific attributes of the `spiderman` object.

This is the power of methods: they allow our objects to have behavior and interact with the world in our program.

## Challenge
Have a look at the skeleton code of the `Pet` class and complete the following tasks:

1: In the `feed` method:

- Decrease the pet's `hunger` by 1
- Print a message saying the pet has been fed


2: Outside the class:

- Call the `feed` method three times on `my_pet`
- After each call to `feed`, print the current hunger level of `my_pet`.

After completing the task your code should give the following expected output.
## Expected Output

```
Fluffy has been fed.
Fluffy's hunger level: 4
Fluffy has been fed.
Fluffy's hunger level: 3
Fluffy has been fed.
Fluffy's hunger level: 2
Fluffy's final hunger level: 2
```