# Lesson 4: Understanding the `__init__`method
In this lesson, we'll cover:
- The role of the `__init__` method
- How `self` and `__init__` work together in object creation
- Hands-on challenge: Implement the `__init__` method for a Pet class

## The role of the`__init__` method

Now, let's talk about that special `__init__` method we've been using. The `__init__` method is a special method in Python classes, also known as a constructor. Its job is to initialize the attributes of a new object when it's created.

```python
class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
```

The `__init__` method is automatically called when we create a new object from our class. It sets up the initial state of the object.

In our `SuperHero` class, `__init__` is responsible for setting the initial values for `name`, `power`, `health`, and `speed` for each new superhero we create.

## How `self` and `__init__`work together in object creation

When we create a new object in Python, the language automatically calls the `__init__` method of the class. This method initializes the newly created object. Let's break it down:

- When we create an object: `object = ClassName(arg1, arg2, ...)`
- In your mind, think of this as if we had written: `ClassName.__init__(object, arg1, arg2, ...)`

Let's see this with our `SuperHero` class:

```python
# Creating a superhero
iron_man = SuperHero("Iron Man", "repulsor beams", 110, 80)
```

Here's what's happening behind the scenes:

1. Python creates a new, empty object.
2. Visualize this as if we have called `SuperHero.__init__(iron_man, "Iron Man", "repulsor beams", 110, 80)`
   * `self` inside `__init__` refers to the new `iron_man` object
   * The other parameters (`name`, `power`, `health`, `speed`) are filled with the values we provided

After this process, `iron_man` is a fully initialized `SuperHero` object with all its attributes set.


- In method definitions (including `__init__`), we always include `self` as the first parameter.
- When creating objects or calling methods, we don't provide `self` - Python does it automatically.


## Challenge: Implement the Pet __init__ Method

We have a `Pet` class with attributes already defined, but its `__init__` method is missing. Currently, the code will produce the following error when you try to run it.

```
TypeError: Pet() takes no arguments
```
## Your Task:
**Implement the `__init__` method**: Add the `__init__` method to the `Pet` class to initialize the `name`, `species`, and `age` attributes when a new pet is created.

## Expected Output

After implementing the `__init__` method correctly, running the code should produce this output:

```
Fluffy is a 3-year-old cat.
Buddy is a 2-year-old dog.
```

## Hints

- The `__init__` method is called automatically when creating a new object.
- Think about the parameters the `__init__` method should have.