# Lesson 5: Docstrings for Classes and Methods (Optional)

In this lesson, we'll cover:

- What docstrings are and why they matter
- How to write docstrings for classes and methods
- Best practices for effective docstrings
- How to use docstrings in Python
- Hands-on challenge: Write docstrings for a Pet class and its methods

## Definition
*Docstrings are string literals that describe functions, methods, classes, or modules.* They provide essential documentation for our code.

## Example

```python
class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main power
        health (int): The superhero's health points
        speed (int): The superhero's speed rating
    """

    def __init__(self, name, power, health, speed):
        """Initialize a new SuperHero instance."""
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

    def use_power(self):
        """Make the superhero use their power."""
        print(f"{self.name} uses {self.power}!")

    def take_damage(self, amount):
        """
        Reduce the superhero's health by the given amount.

        Args:
            amount (int): The amount of damage to inflict
        """
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")
```

## Writing Docstrings

For both classes and methods:
- Write immediately after the definition
- Use triple quotes (""") to enclose the docstring
- Follow a consistent style (e.g., [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html))

For classes:
- Describe the purpose of the class
- List and explain attributes

For methods:
- Use a one-line description for simple methods
- For complex methods:
  - Describe what the method does
  - List and explain parameters (Args:)
  - Describe the return value (Returns:)
  - Mention any exceptions raised (Raises:)

## Using Docstrings

```python
# Print the class docstring
print(SuperHero.__doc__)

# Get help on the class (includes docstrings)
help(SuperHero)

# Print a method's docstring
print(SuperHero.take_damage.__doc__)
```

By adding docstrings, you make your code more understandable for future users, including yourself.

## Challenge

Add a docstrings to the following code:


# Task:
1. Write a class docstring describing what the `Pet` class represents.
2. Add a brief docstring to the `__init__` method.
3. Add a docstring to the `make_sound` method explaining what it does.

Remember to use triple quotes for your docstrings!

**Note:** Initially, when you run this code, you'll see `None` printed for each docstring because they don't exist yet. This is normal! Your task is to add the docstrings so that you see your documentation instead of None.