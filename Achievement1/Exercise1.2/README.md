# Exercise 1.2: Data Types in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [The IPython Shell](#the-ipython-shell)
4. [Variables & Data Types in Python](#variables--data-types-in-python)
    - [Scalar Objects](#scalar-objects)
    - [Non-Scalar Objects](#non-scalar-objects)
    - [Tuples](#tuples)
    - [Lists](#lists)
    - [Strings](#strings)
    - [Dictionaries](#dictionaries)
5. [Task Steps](#task-steps)
    - [Step 1: Recipe Structure](#step-1-recipe-structure)
    - [Step 2: Recipe Example](#step-2-recipe-example)
    - [Step 3: All Recipes Structure](#step-3-all-recipes-structure)
    - [Step 4: More Recipes](#step-4-more-recipes)
    - [Step 5: Print Ingredients](#step-5-print-ingredients)
6. [Learning Journal](#learning-journal)
7. [Screenshots](#screenshots)
8. [Summary](#summary)

## Introduction

Python programming involves understanding various data types and structures. This document provides an overview of these, with a focus on their application in a Recipe app.

## Learning Goals

- Explain variables and data types in Python.
- Summarize the use of objects in Python.
- Create a data structure for your Recipe app.

## The IPython Shell

The IPython shell is a powerful tool for interactive Python programming, offering enhanced features over the standard Python shell.

## Variables & Data Types in Python

Python variables can hold a variety of data types, each suited for different purposes in programming.

### Scalar Objects

Scalar objects in Python are indivisible units that hold a single value. Examples include:

- Integers (`int`): Whole numbers.
- Floating-point (`float`): Decimal numbers.
- Booleans (`bool`): True or False values.

Example:

```python
number = 5  # int
decimal = 3.14  # float
condition = True  # bool
```

### Non-Scalar Objects

Non-scalar objects can hold multiple values and include data structures like lists, tuples, and dictionaries.

### Tuples

Tuples are immutable sequences, typically used to store collections of heterogeneous data.

Example:

```python
fruit_tuple = ("apple", "banana", "cherry")
```

Visual: A series of connected boxes, each containing a fruit name.

### Lists

Lists are mutable sequences, ideal for storing collections of homogeneous items that might change over time.

Example:

```python
fruit_list = ["apple", "banana", "cherry"]
```

Visual: A flexible line of boxes, each containing a fruit name, with the ability to add or remove boxes.

### Strings

Strings are sequences of characters, used for storing text.

Example:

```python
greeting = "Hello, I am a string"
```

Visual: A series of connected character boxes forming a sentence.

### Dictionaries

Dictionaries are key-value pairs, useful for associating unique keys with specific values.

Example:

```python
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.0}
```

Visual: A set of paired boxes, each pair containing a fruit name and its price.

## Task Steps

### Step 1: Recipe Structure

```python
recipe_1 = {
    "name": str,
    "cooking_time": int,
    "ingredients": [list]
}
```

For the recipe_1 structure, a dictionary is the ideal choice due to its inherent ability to store data in key-value pairs. This aligns perfectly with our need to represent each attribute of a recipe—such as its name, cooking time, and ingredients—with clarity and accessibility. In a dictionary, the keys (name, cooking_time, ingredients) provide a descriptive and readable way to access their respective values. This not only enhances the readability of our code but also simplifies data retrieval and manipulation. Dictionaries in Python are mutable, meaning we can easily modify or update the recipe information as needed, such as adding or changing ingredients, which is essential in dynamic applications like a Recipe app.

### Step 2: Recipe Example

```python
recipe_1 = {
    "name": "tea",
    "cooking_time": 5,
    "ingredients": ["tea leaves", "sugar", "water"]
}
```

### Step 3: All Recipes Structure

```python
all_recipes = [recipe_1]
```

The all_recipes structure is implemented as a list, which is an ideal choice for storing a collection of recipes in a sequential and ordered manner. Lists in Python are highly flexible and allow us to easily add, remove, or modify elements, which in this case are individual recipe dictionaries. By using a list, we can maintain the recipes in an organized sequence, enabling easy access, iteration, and manipulation of each recipe. This approach not only facilitates efficient data handling, especially when dealing with multiple recipes, but also ensures scalability. As our Recipe app grows to include more recipes, the list structure will efficiently accommodate this expansion, allowing us to dynamically append new recipes or modify existing ones.

### Step 4: More Recipes

```python
recipe_2 = {
    "name": "lemon garlic shrimp pasta",
    "cooking_time": 25,
    "ingredients": ["spaghetti", "shrimp", "garlic", "lemon", "parsley", "olive oil", "chili flakes", "parmesan cheese"]
}

recipe_3 = {
    "name": "beef tacos",
    "cooking_time": 30,
    "ingredients": ["ground beef", "taco seasoning", "corn tortillas", "lettuce", "tomato", "cheese", "sour cream", "salsa"]
}

recipe_4 = {
    "name": "vegetable stir-fry",
    "cooking_time": 25,
    "ingredients": ["bell peppers", "broccoli", "carrots", "snow peas", "garlic", "soy sauce", "ginger", "sesame oil", "tofu"]
}

recipe_5 = {
    "name": "chicken caesar salad",
    "cooking_time": 15,
    "ingredients": ["romaine leetuce", "grilled chicken breast", "croutons", "parmesan cheese", "caesar dressing", "lemon juice"]
}
```

### Step 5: Print Ingredients

print([recipe["ingredients"] for recipe in recipes])

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- A Screenshot demonstrating each step of the process is included in the repository, appropriately named `All-Steps.png`.

## Summary

This exercise provides an overview of Python's data types and structures, essential for organizing and manipulating data in programming tasks like building a Recipe app.
