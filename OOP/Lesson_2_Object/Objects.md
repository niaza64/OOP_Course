# Lesson 2: Understanding Objects

In this lesson, we'll cover:
- What are objects
- How we've already been creating objects
- Understanding the code for creating objects
- Accessing and modifying object attributes
- The importance of parameter order
- Hands-on challenge: Create a Pet object and modify its attributes

## What are objects

Let's start with a formal definition of an object.

*An object is an instance of a class. It's a specific item created using the blueprint defined by the class.*

## We've already been creating objects!

Let's look at the full example from our previous lesson:

```python
class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

# Creating superhero objects
iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
spider_man = SuperHero("Spider Man", "web slinging", 90, 95)
thor = SuperHero("Thor", "lightning control", 120, 70)
```

In those last three lines, we were already creating objects! We've been making superheroes all along, and now we're just giving this process a programming name: object creation or instantiation.

Let's relate this to our definition of objects:
- The `SuperHero` class is our blueprint.
- Each superhero we create (like Iron Man, Spider Man, or Thor) is an object or instance of the `SuperHero` class.

## Understanding the code for creating objects

When we write `iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)`, we're telling Python:
- Use the `SuperHero` blueprint
- Create a new superhero object
- Set its `name` to "Iron Man", `power` to "repulsor beams", `health` to 100, and `speed` to 80
- Store this new superhero object in a variable called `iron_man`

Don't worry about `__init__` and `self` for now. Just know that this special method helps set up our new superhero with the right characteristics.

## Accessing and modifying object attributes

Once we've created our superhero objects, we can access and modify their attributes using dot notation. Here's how:

```python
# Accessing attributes
print(iron_man.name)  # Output: Iron Man
print(spider_man.power)  # Output: web slinging
print(thor.health)  # Output: 120

# Modifying attributes
iron_man.health = 90
spider_man.speed = 100
thor.power = "thunder and lightning"

# Checking the modified attributes
print(iron_man.health)  # Output: 90
print(spider_man.speed)  # Output: 100
print(thor.power)  # Output: thunder and lightning
```

We use the object's name, followed by a dot, followed by the attribute name to access or modify an attribute. This allows us to interact with our superhero objects and change their characteristics as needed in our program.

## The importance of parameter order

When creating a new superhero object, the order of the values we provide is crucial. It must match the order in the `__init__` method of our `SuperHero` class. Let's look at our `__init__` method again:

```python
def __init__(self, name, power, health, speed):
    self.name = name
    self.power = power
    self.health = health
    self.speed = speed
```

Now, let's create two superhero objects:

```python
# Correct order
correct_hero = SuperHero("Captain America", "super strength", 110, 85)

# Incorrect order
incorrect_hero = SuperHero(100, "Hulk", 75, "gamma radiation")
```

In the `correct_hero` example, we're providing the arguments in the correct order: name, power, health, speed.

However, in the `incorrect_hero` example, we've mixed up the order. As a result:
- `name` gets assigned 100 (a number instead of a string)
- `power` gets assigned "Hulk" (which is actually the name)
- `health` gets assigned 75 (correct type, but meant to be the speed)
- `speed` gets assigned "gamma radiation" (a string instead of a number, and actually the power)

Python won't give us any errors for this incorrect order, which means we need to be careful when creating our objects!


## Challenge
Using the provided `Pet` class, complete the following tasks:

- Create a pet named `Whiskers` that is a cat with `hunger` level 6 and `energy` level 8.
- Print Whiskers' initial attributes.
- Modify Whiskers' attributes:
   - Decrease hunger by 3
   - Increase energy by 2
- Print Whiskers' modified attributes.

## Expected Output
```
Initial Attributes: Whiskers (cat) - Hunger: 6, Energy: 8

Modified Attributes: Whiskers (cat) - Hunger: 3, Energy: 10
```
Hints:
- Create object: `pet_name = Pet("Name", "species", hunger_value, energy_value)`
- Access attributes: `pet_name.attribute`
- Modify attributes: `pet_name.attribute = new_value` or `pet_name.attribute += value`
- Print format: `f"{pet.name} ({pet.species}) - Hunger: {pet.hunger}, Energy: {pet.energy}"`