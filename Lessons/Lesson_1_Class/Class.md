# Lesson 1: Introduction to Classes

In this lesson, we'll cover:

- The concept of classes and why we use them
- Basic syntax for defining a class in Python
- Creating a simple SuperHero class
- How classes make our code more efficient and organized
- Hands-on challenge: Build your first Pet class

## What are classes and why do we use them?

Imagine you're a game developer creating an epic superhero adventure game. You start by defining individual heroes:

```python
hero_1_name = "Iron Man"
hero_1_power = "repulsor beams"
hero_1_health = 100
hero_1_speed = 80

hero_2_name = "Spider Man"
hero_2_power = "web slinging"
hero_2_health = 90
hero_2_speed = 95

hero_3_name = "Thor"
hero_3_power = "lightning control"
hero_3_health = 120
hero_3_speed = 70
```

Whoa! That's a lot of lines just for three heroes. And what if you want to add more attributes like "strength" or "intelligence"? Or what if you need to create 50 different heroes? Your code would become messy very easily. You would wonder how you could avoid this.

This is where classes come to the rescue.

## Definition

*A class is a blueprint for creating objects (superheroes in our case) with shared characteristics.*

Think of it this way: if you were building houses, you wouldn't design each brick individually. Instead, you'd have a blueprint for a standard brick, and then use that to make as many bricks as you need. Classes in programming work similarly - they're blueprints for creating many similar objects efficiently.

In our example, instead of defining each hero individually, we can create a single blueprint that describes what characteristics every superhero should have, and use this blueprint to create superheroes.

In programming terms, these characteristics are called "attributes" (like name, power, health, speed).

Our superhero blueprint (class) will define these attributes. Then, we can use this blueprint to create as many superheroes as we want, quickly and easily.

## Basic syntax for defining a class

Here's the basic syntax for defining a class (our superhero blueprint) in Python:

```python
class ClassName:
    def __init__(self, param1, param2, ...):
        self.attribute1 = param1
        self.attribute2 = param2
        # ...
```

In Python, a class is defined with the special word `class` followed by the name of the class.

It's important to note that class names in Python use PascalCase convention, meaning each word starts with a capital letter and there are no underscores between words (e.g., SuperHero, IronMan, SpiderMan).

For now, just think of `def __init__` as a way to set up the initial characteristics of our superhero. We'll explain it in more detail in upcoming lesson.

## Creating a simple SuperHero class

Let's see how we can use a class to create our superhero blueprint:

```python
class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

# Now, creating heroes is easy!
iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
spider_man = SuperHero("Spider Man", "web slinging", 90, 95)
thor = SuperHero("Thor", "lightning control", 120, 70)
```

Ta-da! We've created a superhero blueprint (our `SuperHero` class) and used it to create three superheroes. It's so much cleaner and easier to manage. Don't worry if you don't understand all the syntax here, especially the part where we're creating individual superheroes. We'll dive into the details of how to use this blueprint in our next lesson.

For now, just focus on the idea that we've created a single blueprint that defines what a superhero is, and that we can use this blueprint to create many different superheroes.

## How classes make our code more efficient

Using this blueprint approach helps us in several ways:
- We can create many heroes quickly without repeating code.
- All hero information (attributes) is organized in one place.
- We can easily add new characteristics to all heroes by updating the blueprint.
- Our code becomes easier to read and understand.


## Challenge: Create a Pet Class

Have a look at the skeleton code and complete the following tasks:

1. Define a class named `Pet`.
2. Use the `def __init__(self, name, species)` method to help you with initialization.
3. Inside the `__init__` method, set up two attributes:
   - `name`: assigned the value of the `name` parameter
   - `species`: assigned the value of the `species` parameter

## Expected Output
```
My pet is a cat named Fluffy
```
Hints:
- Class definitions start with the `class` keyword
- Use `self.attribute_name` to create attributes inside the class

