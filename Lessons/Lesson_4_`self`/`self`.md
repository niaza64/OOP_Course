# Lesson 4: Understanding `self` in Python

In this lesson, we'll cover:
- The purpose and importance of `self`
- How `self` works in method calls
- The role of the `__init__` method
- How `self` and `__init__` work together in object creation
- Hands-on challenge: Fix a method by correctly using 'self'

## The purpose and importance of `self`

Remember our superhero team? We have many superheroes, each with their own powers and attributes. When we create a superhero or call a method, how does Python know which superhero we're talking about? This is where `self` comes in!

Let's define it:

*`self` is how Python refers to the specific object (superhero) being created or acted upon. It allows each superhero to have their own set of attributes and use their own powers.*

Let's look at our `SuperHero` class again:

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

Notice how `self` is the **first** parameter in all our methods, including `__init__`. This is a Python convention and is crucial for the proper functioning of classes.

## How `self` works in method calls

To better understand how `self` works, it can be helpful to visualize method calls in a different way:

- When we call a method: `object.method()`. In your mind think of this as if we had written: `ClassName.method(object)`

Let's see this in action with our superhero example:

```python
# Creating superheroes
spider_man = SuperHero("Spider-Man", "web-slinging", 100, 90)
wonder_woman = SuperHero("Wonder Woman", "super strength", 120, 85)

# Using their powers
spider_man.use_power() 
# Spider-Man uses web-slinging!
wonder_woman.use_power()
# Wonder Woman uses super strength!
```

Here's what's happening behind the scenes:

1. When we call `spider_man.use_power()`:
   * Visualize this as if we have called `SuperHero.use_power(spider_man)`
   * `self` inside `use_power()` refers to `spider_man`

2. When we call `wonder_woman.use_power()`:
   * Visualize this as if we have called `SuperHero.use_power(wonder_woman)`
   * `self` inside `use_power()` refers to `wonder_woman`

This mechanism allows each superhero to perform actions specific to itself, using its own attributes.

# Challenge: Fix the Superhero Power Boost Method

## The Problem

We have a `Superhero` class with a `power_boost` method that's not working correctly. Your task is to identify the issue and fix it.

When you run this code, you'll encounter the following error:

```
TypeError: power_boost() takes 1 positional argument but 2 were given
```

## Your Task

**Fix the Bug**: Modify the `power_boost` method to make it work correctly.

## Expected Output

After fixing the code, running it should produce this output:

```
Iron Man's strength increased to 100!
```

## Hints

- Think about the role of `self` in class methods.
- Consider how instance attributes are accessed within a method.

*Remember: With great power comes great responsibility... and proper use of `self`!*