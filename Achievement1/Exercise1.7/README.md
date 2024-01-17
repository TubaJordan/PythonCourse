# Exercise 1.7: Implementing Object-Relational Mapping with SQLAlchemy

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [What is an Object-Relational Mapper?](#what-is-an-object-relational-mapper)
4. [Setting Up SQLAlchemy](#setting-up-sqlalchemy)
   - [Installation](#installation)
   - [Database Connector Package](#database-connector-package)
5. [Checking MySQL Server Status and Connecting SQLAlchemy](#checking-mysql-server-status-and-connecting-sqlalchemy)
   - [MySQL on Ubuntu](#mysql-on-ubuntu)
   - [MySQL on macOS](#mysql-on-macos)
   - [MySQL on Windows](#mysql-on-windows)
6. [Connecting SQLAlchemy to Database](#connecting-sqlalchemy-to-database)
7. [Creating a Table from a Mapped Class](#creating-a-table-from-a-mapped-class)
   - [Introduction to Declarative Base](#introduction-to-declarative-base)
   - [Defining the ORM Model](#defining-the-orm-model)
   - [Representing the Model](#representing-the-model)
   - [Creating the Table](#creating-the-table)
   - [Verifying Table Creation](#verifying-table-creation)
8. [Creating a Session for Your Database](#creating-a-session-for-your-database)
   - [Overview of Session Object](#overview-of-session-object)
   - [Importing Sessionmaker](#importing-sessionmaker)
   - [Binding Session to Engine](#binding-session-to-engine)
   - [Initializing Session Object](#initializing-session-object)
   - [Usage of Session in ORM](#usage-of-session-in-orm)
9. [Adding Entries to Your Table](#adding-entries-to-your-table)
10. [Reading Entries from a Table](#reading-entries-from-a-table)
11. [Updating Entries in Your Table](#updating-entries-in-your-table)
12. [Deleting Entries from Your Table](#deleting-entries-from-your-table)
13. [Building Your Command Line Recipe App](#building-your-command-line-recipe-app)
    - [Overview of the App Development Process](#overview-of-the-app-development-process)
    - [Key Guidelines for Development](#key-guidelines-for-development)
    - [Flowchart and Application Structure](#flowchart-and-application-structure)
14. [Task](#task)
    - [Part 1: Set Up Your Script & SQLAlchemy](#part-1-set-up-your-script--sqlalchemy)
    - [Part 2: Create Your Model and Table](#part-2-create-your-model-and-table)
    - [Part 3: Define Main Operations](#part-3-define-main-operations)
    - [Part 4: Design Your Main Menu](#part-4-design-your-main-menu)
    - [Part 5: Final Steps](#part-5-final-steps)
15. [Learning Journal](#learning-journal)
16. [Screenshots](#screenshots)
17. [Summary](#summary)

## Introduction

This exercise focuses on finalizing the Recipe Application using object-relational mapping (ORM) with SQLAlchemy. Object-relational mapping is a technique for converting data between incompatible systems using object-oriented programming languages. This exercise will introduce SQLAlchemy, a Python SQL toolkit and ORM, which allows for a Pythonic way of interacting with databases.

## Learning Goals

- Understand the concept and advantages of using an Object-Relational Mapper.
- Set up SQLAlchemy to interact with a database.
- Perform database operations using SQLAlchemy, including creating tables, adding, reading, updating, and deleting entries.
- Develop the final version of the command line Recipe application using SQLAlchemy.

## What is an Object-Relational Mapper?

An object-relational mapper (ORM) is a tool that facilitates the interaction between an object-oriented programming language and a relational database. Traditional database operations often require familiarity with SQL queries, which can vary across different Database Management Systems (DBMSs). ORM simplifies this process by enabling interactions with the database using the programming language's syntax and structures.

For example, in a conventional approach, inserting a record into a database might involve a SQL command like this:

```python
cursor.execute('''INSERT INTO products
    (product_id, product_name, category, price)
    VALUES (101, 'Notebook', 'Stationery', 3.99)
    ''')
```

With an ORM, this operation is expressed in a more intuitive, object-oriented manner:

```python
new_product = Product(product_id=101, product_name="Notebook", category="Stationery", price=3.99)
session.add(new_product)
session.commit()
```

In this ORM approach, `Product` is a class corresponding to a database table, and `new_product` is an instance of this class. The ORM handles the conversion of this object-oriented operation into the appropriate SQL command.

This method not only makes code more readable but also reduces the need for direct SQL knowledge, especially when moving between different DBMSs. ORMs like SQLAlchemy in Python offer a seamless way to integrate database operations into application development, aligning with the Pythonic emphasis on readability and efficiency.

SQLAlchemy, as an open-source Python SQL toolkit, provides extensive ORM functionalities. It's commonly used in various frameworks, including those that don't have built-in ORM support, like Flask. Embracing ORMs in development, particularly in web frameworks such as Django, simplifies database interactions, allowing developers to focus more on application logic rather than database syntax.

## Setting Up SQLAlchemy

### Installation

To install SQLAlchemy, run the following command:

```bash
pip install sqlalchemy
```

This installs SQLAlchemy, enabling Python applications to communicate with databases in an object-oriented manner.

### Database Connector Package

For connecting SQLAlchemy to a MySQL database, install the `mysqlclient` package:

```bash
pip install mysqlclient
```

This package serves as the link between SQLAlchemy and MySQL, facilitating database operations.

With these installations, SQLAlchemy is set up and ready for integration into Python applications, allowing for database interactions using object-relational mapping. The next steps involve configuring SQLAlchemy to connect to the database.

## Checking MySQL Server Status and Connecting SQLAlchemy

MySQL Server Status Check

### MySQL on Ubuntu

- Use `systemctl` to check the MySQL status:

```bash
sudo systemctl status mysql
```

- If MySQL is not running, start it with:

```bash
sudo systemctl start mysql
```

### MySQL on macOS

- Access MySQL through System Preferences.
- Check the server status; if it's not running, start the server.

### MySQL on Windows

- Access "Services" via `services.msc` in the Run dialog (`Windows + R`).
- Look for the MySQL service and check if it's running. Start it if necessary.

## Connecting SQLAlchemy to Database

1. **Open an IPython Shell** and import `create_engine` from SQLAlchemy:

```python
from sqlalchemy import create_engine
```

2. **Create the Connection URL:**
The URL format is:

```python
<database type>://<username>:<password>@<hostname>/<database name>
```

For a MySQL database named `my_database` with username `cf-python` and password `password`, the URL is:

```python
mysql://cf-python:password@localhost/my_database
```

3. **Initialize Engine:**
Create an engine object to connect to the database:

```python
engine = create_engine("mysql://cf-python:password@localhost/my_database")
```

This `engine` object is used for database interactions, similar to the `conn` object from previous exercises.

The setup ensures that the MySQL server is running and SQLAlchemy is connected to the database, paving the way for ORM-based database operations.

## Creating a Table from a Mapped Class

### Introduction to Declarative Base

SQLAlchemy utilizes a Declarative Base class to define database tables. This class acts as a foundation for creating ORM models.

Import Declarative Base

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

The `Base` class is now ready to be inherited by ORM models.

### Defining the ORM Model

The model represents a database table. For example, to create a `Book` table:

Import Required Modules

```python
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
```

Define the Model

```python
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    author = Column(String(50))
    published_year = Column(Integer)
    genre = Column(String(50))
```

- `__tablename__` sets the table name in the database.
- `Column` objects define table columns, specifying data types and constraints.
- `Integer` and `String` data types correspond to SQL data types.

### Representing the Model

The `__repr__` method provides a readable representation of ORM objects:

```python
def __repr__(self):
    return f"<Book(id={self.id}, title='{self.title}')>"
```

### Creating the Table

The model alone doesn't create a table in the database. Execute `create_all()`:

```python
Base.metadata.create_all(engine)
```

This command constructs the table as defined in the model.

### Verifying Table Creation

After running `create_all()`, verify the table's existence:

Open MySQL Command Line Interface:

```bash
mysql -u username -p
```

Check Tables:

```sql
USE my_database;
SHOW TABLES;
```

The `books` table should be listed.

Inspect Table Structure:

```sql
DESCRIBE books;
```

This command displays the columns and types, mirroring the ORM model.

## Creating a Session for Your Database

### Overview of Session Object

A session in SQLAlchemy serves as a conduit for database operations, similar to a cursor used in traditional SQL interactions. The session facilitates object-oriented database manipulation, contrasting with the direct SQL query approach.

### Importing Sessionmaker

To begin creating a session, the `sessionmaker` function from SQLAlchemy is essential:

```python
from sqlalchemy.orm import sessionmaker
```

This function will be used to generate the `Session` class.

### Binding Session to Engine

The `Session` class connects to the database through the engine. This connection is established by binding the session to the engine:

```python
Session = sessionmaker(bind=engine)
```

The `engine` variable references the database engine created earlier.

### Initializing Session Object

With the `Session` class ready, instantiate a session object:

```python
session = Session()
```

This session object will be the primary tool for conducting database operations.

### Usage of Session in ORM

The session object allows for adding, querying, updating, and deleting database entries using the defined ORM models. For instance, to add a new book entry to a `books` table, the process would be:

```python
new_book = Book(title="Example Title", author="Author Name", published_year=2020, genre="Fiction")
session.add(new_book)
session.commit()
```

Here, `new_book` is an instance of the `Book` class, representing a row in the `books` table. The `session.add()` method stages the new book for insertion, and `session.commit()` finalizes the transaction, persisting the changes to the database.

In summary, the session in SQLAlchemy abstracts database transactions, allowing for a more intuitive and Pythonic approach to database management.

## Adding Entries to Your Table

### Creating Objects from the ORM Model

With the ORM model defined, new instances of the model can be created to represent rows in the database. For example, to add a new recipe for "Pasta":

```python
pasta = Recipe(name="Pasta", cooking_time=30, ingredients="Pasta, Tomato Sauce, Cheese")
```

This code snippet creates an object `pasta`, an instance of the `Recipe` class, corresponding to a row in the database.

### Adding the Entry to the Database

To add this new recipe to the database:

```python
session.add(pasta)
```

The `session.add()` function stages the `pasta` object for insertion into the database.

### Committing the Entry

To finalize the addition and persist the changes in the database:

```python
session.commit()
```

Committing the session ensures that the `pasta` recipe is stored in the database.

### Verifying the Addition

To confirm the entry of the new recipe into the database, a simple SQL query can be executed using the MySQL command line client:

```sql
SELECT * FROM practice_recipes;
```

The output should display the newly added pasta recipe, along with any other existing entries in the `practice_recipes` table.

This process of adding entries demonstrates the simplicity and efficiency of using ORM for database operations.

## Reading Entries from a Table

### Querying the Database

SQLAlchemy's session object provides the `query()` method for database operations. This method enables the retrieval of database entries as objects, offering an alternative to SQL's `SELECT` query.

### Basic Query

To retrieve all entries from a table, the `all()` method is used:

```python
recipes = session.query(Recipe).all()
```

This returns a list of `Recipe` objects representing each row in the `Recipe` table.

### Accessing Object Attributes

The attributes of these objects can be accessed using dot notation:

```python
for recipe in recipes:
    print(f"ID: {recipe.id}, Name: {recipe.name}, Ingredients: {recipe.ingredients}")
```

### Retrieving a Single Object

For retrieving a specific entry by its primary key:

```python
specific_recipe = session.query(Recipe).get(1)
```

This returns the `Recipe` object with an ID of 1.

### Filtering Results

The `filter()` method applies conditions to queries, analogous to SQL's `WHERE` clause:

```python
coffee_recipes = session.query(Recipe).filter(Recipe.name == "Coffee").all()
```

This returns all recipes where the name is "Coffee".

### Using LIKE for Pattern Matching

The `like()` method within `filter()` enables pattern matching:

```python
recipes_with_water = session.query(Recipe).filter(Recipe.ingredients.like("%Water%")).all()
```

This query fetches recipes with "Water" in their ingredients.

### Combining Conditions

Multiple conditions can be combined:

```python
complex_query = session.query(Recipe).filter(Recipe.ingredients.like("%Milk%"), Recipe.ingredients.like("%Baking Powder%")).all()
```

This retrieves recipes containing both "Milk" and "Baking Powder".

### Implementing Practice

For practice, one can try using the `filter()` method to find recipes containing a specific ingredient like "sugar". The results can then be reviewed to enhance understanding of SQLAlchemy's querying capabilities.

## Updating Entries in Your Table

### Steps for Updating Rows

Updating database entries using an ORM involves a few key steps:

1. Retrieve the desired object(s) from the table.
2. Modify the necessary attributes of the object.
3. Commit the changes to persist them in the database.

Example: Modifying a Recipe

Consider modifying a recipe for "Pasta" to include a new ingredient:

```python
# Retrieve the Pasta recipe
pasta_recipe = session.query(Recipe).filter(Recipe.name == "Pasta").first()

# Check current ingredients
print(f"Current ingredients: {pasta_recipe.ingredients}")

# Add a new ingredient
pasta_recipe.ingredients += ", Olive Oil"

# Verify the change
print(f"Updated ingredients: {pasta_recipe.ingredients}")

# Commit the changes
session.commit()
```

This code updates the 'Pasta' recipe by adding 'Olive Oil' to its ingredient list.

### Direct Database Updates

In situations where multiple rows need updating, SQLAlchemy provides a method to make direct changes:

```python
# Update all Cake recipes to Birthday Cake
session.query(Recipe).filter(Recipe.name == "Cake").update({Recipe.name: "Birthday Cake"})
session.commit()
```

This command changes the name of all entries with "Cake" to "Birthday Cake".

### Verifying Changes

After committing updates, verify the changes in the database:

```sql
SELECT * FROM practice_recipes WHERE name = 'Birthday Cake';
```

This SQL query checks if the name change to "Birthday Cake" has been reflected in the database.

### Practice Opportunity

A good practice exercise is to modify another recipe, such as changing the ingredients of a "Cake" recipe to include "Chocolate Powder". This exercise reinforces understanding of updating entries using SQLAlchemy's ORM.

## Deleting Entries from Your Table

### Deleting Rows through ORM

SQLAlchemy's ORM simplifies the deletion of rows from a database table. The process involves retrieving the desired entry as an object and then using the `delete()` method.

Example: Adding and Deleting an Entry
Consider adding a new recipe for "Sandwich" and then deleting it:

```python
# Add a new recipe for Sandwich
sandwich = Recipe(name="Sandwich", ingredients="Bread, Cheese, Ham", cooking_time=5)
session.add(sandwich)
session.commit()

# Retrieve and delete the Sandwich recipe
sandwich_to_delete = session.query(Recipe).filter(Recipe.name == "Sandwich").one()
session.delete(sandwich_to_delete)
session.commit()
```

This code adds a 'Sandwich' recipe to the table, then subsequently deletes it.

### Verifying Deletion

To confirm the deletion:

```python
# List all recipe names
all_recipe_names = session.query(Recipe.name).all()
print(all_recipe_names)
```

This code lists all the names of the recipes remaining in the table, ensuring "Sandwich" is no longer present.

### Enhanced Output with Specific Columns

For a more detailed view of the entries, including specific columns:

```python
# Retrieving specific columns
recipe_details = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
print(recipe_details)
```

This command displays the IDs and names of all the recipes, offering a concise overview of the table's contents.

In summary, the deletion of entries via SQLAlchemy's ORM is straightforward and efficient, complementing the overall ORM operations for database management.

## Building Your Command Line Recipe App

### Overview of the App Development Process

Building a command line Recipe App is an exercise in applying Python skills, with a particular focus on SQLAlchemy for database operations and handling user input.

### Key Guidelines for Development

1. Code Readability:

    - Ensure to comment throughout the code, providing clear explanations of functions and logic.

2. Creating Custom Recipes:

    - Implement functionality to create and add personal recipes to the database through the application.

3. Code Testing and Integrity:

    - Thoroughly test the application with both expected and unexpected inputs to ensure robustness.
    - Handle edge cases gracefully without crashing, displaying appropriate error messages and guiding the user back to valid options.

4. User-Friendly Interface:

    - Design the interface to be intuitive and simple, accommodating users without technical backgrounds.
    - Implement validations to guide users correctly through the app's functionalities.

### Flowchart and Application Structure

The flowchart serves as a blueprint, outlining the sequence of operations and user interactions within the app. Key components include:

1. Main Menu:
    - Present a list of options, such as creating, viewing, editing, or deleting recipes.

2. Adding Recipes:
    - Allow users to input details for new recipes and save them to the database.

3. Viewing Recipes:
    - Display a list or specific details of recipes stored in the database.

4. Editing Recipes:
    - Provide options to modify existing recipes, including changing ingredients, cooking time, or recipe names.

5. Deleting Recipes:
    - Enable users to remove recipes from the database.

6. Handling User Inputs:
    - Implement checks for user inputs, ensuring they are valid and handling errors appropriately.

7. Exit Option:
    - Allow users to easily exit the application.

By following these steps and ensuring thorough testing and user-centric design, the Recipe app will serve as a practical demonstration of applied Python programming, database management with SQLAlchemy, and user interface design.

## Task

### Part 1: Set Up Your Script & SQLAlchemy

1. Open Script File:
    - Create a new Python script named `recipe_app.py`.

2. Import Packages:
    - Import necessary packages for SQLAlchemy and database interaction.

```python
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.expression import or_
```

3. Initialize SQLAlchemy:
    - Set up SQLAlchemy with the required database configurations.
    - Create an engine object connected to the specified database.

```python
# Database Configuration: Set up connection parameters for the MySQL database.
USERNAME = "cf-python"
PASSWORD = "password"
HOST = "localhost"
DATABASE = "task_database"

# SQLAlchemy Engine: Create the engine to manage connections to the database.
engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

# Base Class: All model classes will inherit from this class.
Base = declarative_base()
```

4. Create Session Object:
    - Generate and initialize the session object for database transactions.

```python
# Session: Set up the mechanism to talk to the database. 
# The session will be used to query and commit transactions.
Session = sessionmaker(bind=engine)
session = Session()
```

### Part 2: Create Your Model and Table

1. Define Recipe Model:
    - Inherit from the Base class to define the Recipe model.
    - Specify table name and column attributes.
    - Implement `__repr__` and `__str__` methods for object representation.

```python
class Recipe(Base):
    # Table Name: Define the name of the table in the database.
    __tablename__ = "final_recipes"

    # Schema:
    #|-----------------------------------------------------------------------------------|
    #| Field        | Type         | Null     | Key         | Default   | Extra          |
    #|--------------|--------------|----------|-------------|-----------|----------------|
    #| id           | int          | NOT NULL | PRIMARY KEY | NULL      | AUTO_INCREMENT |
    #| name         | varchar(50)  | NULLABLE |             | NULL      |                |
    #| ingredients  | varchar(255) | NULLABLE |             | NULL      |                |
    #| cooking_time | int          | NULLABLE |             | NULL      |                |
    #| difficulty   | varchar(20)  | NULLABLE |             | NULL      |                |
    #|-----------------------------------------------------------------------------------|

    # Columns: Define the structure of the table.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        # Representation: Used for debugging purposes, showing a quick string representation of the object.
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"
    
    def __str__(self):
        # String Representation: Formats recipe details in a user-friendly way for printing.
        ingredients_list = self.ingredients.split(", ")
        formatted_ingredients = "\n ".join(f"  - {ingredient.title()}" for ingredient in ingredients_list)

        return (f"Recipe ID: {self.id}\n"
                f"  Name: {self.name.title()}\n"
                f"  Ingredients:\n {formatted_ingredients}\n"
                f"  Cooking Time: {self.cooking_time} minutes\n"
                f"  Difficulty: {self.difficulty}\n")
    
    def calculate_difficulty(self):
        # Calculate Difficulty: Determines the recipe's difficulty based on cooking time and number of ingredients.
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        # Convert Ingredients to List: Splits the ingredients string into a list for easier manipulation.
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")
```

2. Create Table in Database:
    - Utilize create_all() method to generate the table in the database.

```python
# Create Tables: Execute the creation of tables in the database based on the models defined.   
Base.metadata.create_all(engine)
```

### Part 3: Define Main Operations

1. Function 1: create_recipe():
    - Function to add new recipes to the database.
    - Collect and validate user inputs for recipe details.

```python
def create_recipe():
    # Display the header for the create recipe function.
    print()
    print("==================================================")
    print("           *** Create New Recipes ***             ")
    print("==================================================")
    print("Please follow the steps below to add new recipes!\n")
    
    # Loop to get the number of recipes the user wants to enter.
    # Validates that the input is a positive integer.
    while True:
        try:
            number_of_recipes = int(input("How many recipes would you like to enter? "))
            if number_of_recipes < 1:
                print("Please enter a positive number.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Loop over the number of recipes to be created.
    for i in range(number_of_recipes):
        print(f"\nEnter recipe #{i + 1}")
        print("---------------------")

        # Input validation for recipe name, ensuring it's within the character limit.
        while True:
            name = input("  Enter the recipe name: ").strip()
            if 0 < len(name) <= 50:
                break
            else:
                print("Please enter a valid recipe name (1-50 characters).\n")

        # Input validation for cooking time, ensuring it's a positive integer.
        while True:
            try:
                cooking_time = int(input("  Enter the cooking time in minutes: "))
                if cooking_time > 0:
                    break
                else:
                    print("Please enter a positive number for cooking time.\n")
            except ValueError:
                print("Invalid input. Please enter a positive number for cooking time.\n")

        # Input validation for ingredients, ensuring the input is not empty.
        while True:
                ingredients_input = input("  Enter the recipe's ingredients, separated by a comma: ").strip()
                if ingredients_input:
                    break
                else:
                    print("Please enter at least one ingredient.\n")

        # Create a new recipe instance and add it to the session.
        new_recipe = Recipe(name=name, ingredients=ingredients_input, cooking_time=cooking_time)
        new_recipe.calculate_difficulty()

        # Add the new recipe to the session and attempt to commit it to the database.
        session.add(new_recipe)
        try:
            session.commit()
            print("  ** Recipe successfully added! **")

        except Exception as err:
            # Rollback in case of error during commit.
            session.rollback()
            print("Error occurred: ", err)

    # Display a final message after adding recipes.    
    final_message = "Recipe successfully added!" if number_of_recipes == 1 else "All recipes successfully added!"
    print()
    print("--------------------------------------------------")
    print(f"            {final_message}            ")
    print("--------------------------------------------------\n")
    
    # Pause the execution and wait for the user to press enter.
    pause()
```

2. Function 2: view_all_recipes():
    - Display all recipes from the database.

```python
def view_all_recipes():
    # Retrieve all recipes from the database.
    recipes = session.query(Recipe).all()

    # Check if there are any recipes in the database, and display a message if there are none.
    if not recipes:
        print("***************************************************************")
        print("         There are no recipes in the database to view.         ")
        print("                 Please create a new recipe!                   ")
        print("***************************************************************\n")
        pause()
        return None

    # Header display for viewing all recipes.
    print("=================================================================")
    print("                  *** View All Recipes ***                   ")
    print("=================================================================")

    # Display the number of recipes found.
    recipe_count = len(recipes)
    recipe_word = "recipe" if recipe_count == 1 else "recipes"
    print(f"Displaying {recipe_count} {recipe_word}\n")

    # Loop through each recipe and display its details using a formatted string.
    for i, recipe in enumerate(recipes, start=1):
        print(f"Recipe #{i}\n----------")
        print(format_recipe_for_search(recipe))
        print()
    
    # Footer display after listing all recipes.
    print("\n--------------------------------------------------")
    print("             List Display Successful!              ")
    print("--------------------------------------------------\n")
    
    # Pause the execution and wait for the user to press enter.
    pause()
```

3. Function 3: search_by_ingredients():
    - Search and display recipes based on specified ingredients.

```python
def search_recipe():
    # Retrieve all ingredients from all recipes in the database.
    results = session.query(Recipe.ingredients).all()

    # If no recipes are found, display a message and return to the main menu.
    if not results:
        print("***************************************************************")
        print("       There are no recipes in the database to search.         ")
        print("                 Please create a new recipe!                   ")
        print("***************************************************************\n")
        pause()
        return

    # Initialize a set to store all unique ingredients from the database results.
    all_ingredients = set()
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient.strip())

    # Print header for search function and instructions for user.
    print()
    print("=================================================================")
    print("           *** Search for a Recipe By Ingredient ***             ")
    print("=================================================================")
    print("Please enter a number to see all recipes that use that ingredient\n")

    # Sort and display each unique ingredient with its corresponding index.
    sorted_ingredients = sorted(all_ingredients)
    for i, ingredient in enumerate(sorted_ingredients):
        print(f"{i+1}.) {ingredient.title()}")

    # Prompt user to enter one or more ingredient numbers, separated by spaces.
    print()
    while True:
        try:
            choices = input("Enter ingredient numbers (separate multiple numbers with spaces): ").split()
            selected_indices = [int(choice) for choice in choices]
            if all(1 <= choice <= len(all_ingredients) for choice in selected_indices):
                break
            else:
                print("Please enter numbers within the list range.\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")

    # Convert user input into a list of selected ingredients.
    search_ingredients = [sorted_ingredients[index - 1] for index in selected_indices]

    # Build a search query using the selected ingredients.
    search_conditions = [Recipe.ingredients.ilike(f"%{ingredient}%") for ingredient in search_ingredients]
    search_results = session.query(Recipe).filter(or_(*search_conditions)).all()

    # Format the string of selected ingredients for display.
    if len(search_ingredients) > 1:
        selected_ingredients_str = ", ".join(ingredient.title() for ingredient in search_ingredients[:-1])
        selected_ingredients_str += ", or " + search_ingredients[-1].title()
    else:
        selected_ingredients_str = search_ingredients[0].title()

    # Check if there are any recipes found with the selected ingredients.
    if search_results:
        recipe_count = len(search_results)
        recipe_word = "recipe" if recipe_count == 1 else "recipes"
        print(f"\n{recipe_count} {recipe_word} found containing '{selected_ingredients_str}'\n")
        
        # Display each found recipe with its details.
        for i, recipe in enumerate(search_results, start=1):
            print(f"Recipe #{i}\n----------")
            print(format_recipe_for_search(recipe))
            print()

        # End of search result display with a success message.
        print()
        print("--------------------------------------------------")
        print("            Recipe search successful!             ")
        print("--------------------------------------------------\n")
    else:
        # Message for the user if no matching recipes are found.
        print(f"No recipes found containing '{selected_ingredients_str}'\n")

    # Pause the execution and wait for the user to press enter.
    pause()
```

4. Function 4: update_recipe():
    - Allow users to edit existing recipes in the database.

```python
def update_recipe():
    # Retrieve all recipes from the database.
    recipes = session.query(Recipe).all()

    # Check if there are any recipes in the database; if not, display a message.
    if not recipes:
        print("***************************************************************")
        print("       There are no recipes in the database to update.         ")
        print("                Please create a new recipe!                    ")
        print("***************************************************************\n")
        pause()
        return
    
    # Header for the update function.
    print()
    print("=================================================================")
    print("             *** Update a Recipe By ID Number ***                ")
    print("=================================================================")
    print("Please enter an ID number to update that recipe\n")

    # Display the available recipes for update.
    print("---- Avaiable Recipes ----\n")
    for recipe in recipes:
        print(format_recipe_for_update(recipe))
    print()

    # Loop to get the ID of the recipe to update.
    while True:
        try:
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            recipe_to_update = session.get(Recipe, recipe_id)
            if recipe_to_update:
                break
            else:
                print("No recipe found with the entered ID. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    # Prompt the user to choose which field of the recipe to update.
    print(f"\nWhich field would you like to update for '{recipe_to_update.name}'?")
    print(" - Name")
    print(" - Cooking Time")
    print(" - Ingredients\n")

    # Flag to track whether the field has been successfully updated.
    field_updated = False
    while not field_updated:
        update_field = input("Enter your choice: ").lower()

        # Update logic for each field (name, cooking time, ingredients).
        if update_field == "name":
            while True:
                new_value = input("\nEnter the new name (1-50 characters): ").strip()
                if 0 < len(new_value) <= 50:
                    recipe_to_update.name = new_value
                    field_updated = True
                    break
                else:
                    print("Invalid name. Please enter 1-50 characters.\n")
            break

        elif update_field == "cooking time":
            while True:
                try:
                    new_value = int(input("\nEnter the new cooking time (in minutes): "))
                    if new_value > 0:
                        recipe_to_update.cooking_time = new_value
                        # Recalculate the difficulty after updating the cooking time.
                        recipe_to_update.calculate_difficulty()
                        field_updated = True
                        break
                    else:
                        print("Please enter a positive number for cooking time.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for cooking time.")
            break
                    
        elif update_field == "ingredients":
            while True:
                new_value = input("\nEnter the new ingredients, separated by a comma: ").strip()
                if new_value:
                    # Update the ingredients and recalculate the difficulty.
                    recipe_to_update.ingredients = new_value
                    recipe_to_update.calculate_difficulty()
                    field_updated = True
                    break
                else:
                    print("Please enter at least one ingredient.") 
            break
        else:
            print("Invalid choice. Please choose 'name', 'cooking time', or 'ingredients'.")

    # Attempt to commit the updated recipe to the database.
    try:
        session.commit()
        print("\n--------------------------------------------------")
        print("           Recipe successfully updated!           ")
        print("--------------------------------------------------\n")
    except Exception as err:
        # Rollback in case of error during the commit.
        session.rollback()
        print(f"An error occurred: {err}")

    # Pause the execution and wait for the user to press enter.
    pause()
```

5. Function 5: delete_recipe():
    - Enable deletion of recipes from the database.

```python
def delete_recipe():
    # Retrieve all recipes from the database.
    recipes = session.query(Recipe).all()

    # Check if there are any recipes in the database; if not, display a message.
    if not recipes:
        print("***************************************************************")
        print("        There are no recipes in the database to delete.        ")
        print("                  Please create a new recipe!                  ")
        print("***************************************************************\n")
        pause()
        return
    
    # Header for the delete recipe function.
    print()
    print("=================================================================")
    print("             *** Delete a Recipe By ID Number ***                ")
    print("=================================================================")
    print("Please enter the ID number of the recipe to remove")
    print("** Note: This can NOT be undone **\n")

    # Display the available recipes for deletion.
    print("---- Avaiable Recipes ----\n")
    for recipe in recipes:
        print(format_recipe_for_update(recipe))

    # Loop to get the ID of the recipe to be deleted.
    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to delete: "))
            # Retrieve the recipe to be deleted from the database.
            recipe_to_delete = session.get(Recipe, recipe_id)

            # Confirm deletion from the user.
            if recipe_to_delete:
                confirm = input(f"\nAre you sure you want to delete '{recipe_to_delete.name}'? (Yes/No): ").lower()
                if confirm == "yes":
                    break
                elif confirm == "no":
                    print("Deletion cancelled.\n")
                    pause()
                    return
                else:
                    print("Please answer with 'Yes' or 'No'.")
            else:
                print("No recipe found with the entered ID. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Attempt to delete the selected recipe from the database.
    try:
        session.delete(recipe_to_delete)
        session.commit()
        print()
        print("--------------------------------------------------")
        print("           Recipe successfully deleted!           ")
        print("--------------------------------------------------\n")
    except Exception as err:
        # Rollback in case of error during the deletion.
        session.rollback()
        print(f"An error occured: {err}")

    # Pause the execution and wait for the user to press enter.  
    pause()
```

### Part 4: Design Your Main Menu

1. Implement Main Menu Loop:
    - Create a loop with options for users to interact with the app.
    - Include options for creating, viewing, searching, editing, and deleting recipes.
    - Add an option to quit the application.

```python
def main_menu():
    # Initialize the choice variable.
    choice = ""
    
    # Main menu loop - continues until the user decides to quit the application.
    while choice != "quit":
        
        # Display the main menu header and options.
        print("  _____           _                                   ")
        print(" |  __ \         (_)                /\                ")
        print(" | |__) |___  ___ _ _ __   ___     /  \   _ __  _ __  ")
        print(" |  _  // _ \/ __| | '_ \ / _ \   / /\ \ | '_ \| '_ \ ")
        print(" | | \ \  __/ (__| | |_) |  __/  / ____ \| |_) | |_) |")
        print(" |_|  \_\___|\___|_| .__/ \___| /_/    \_\ .__/| .__/ ")
        print("                   | |                   | |   | |    ")
        print("                   |_|                   |_|   |_|    ")
        print("======================================================")
        print("   What would you like to do? Pick a choice below!    ")
        print("======================================================\n")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe by ingredient")
        print("4. Update an existing recipe")
        print("5. Delete a recipe\n")
        print("Type 'quit' to exit the program\n")
        
        # while True:
            # Get the user's choice and convert it to lower case for easier comparison.
        choice = input("Your choice: ").strip().lower()

        # Execute the appropriate function based on the user's choice.
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            update_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            # Display a goodbye message when the user decides to quit the application.
            print("=============================================")
            print("      Thanks for using the Recipe App!       ")
            print("             See you next time               ")
            print("=============================================")
            break # Exit the loop to terminate the program.
        else:
            # Handle invalid input and prompt the user to try again.
            print("---------------------------------------------------")
            print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 'quit'.")
            print("---------------------------------------------------\n")
            
            # Pause for user acknowledgement before showing the menu again.
            pause()

    session.close()
    engine.dispose()
```

### Part 5: Final Steps

1. Test the Application:
    - Create and interact with recipes using the app.
    - Ensure the app handles both expected and unexpected inputs gracefully.

2. Documentation and Submission:
    - Take screenshots of the app in action.

Task Part 1 - Main Menu
![Task Part 1 - Main Menu](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%201%20-%20Main%20Menu.png)

Task Part 2 - Create Recipes
![Task Part 2 - Create Recipes](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%202%20-%20Create%20Recipes.png)

Task Part 3 - View All Recipes
![Task Part 3 - View All Recipes part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%203%20-%20View%20All%20Recipes%20part%201.png)
![Task Part 3 - View All Recipes part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%203%20-%20View%20All%20Recipes%20part%202.png)

Task Part 4 - Search Recipes
![Task Part 4 - Search Recipes part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%204%20-%20Search%20Recipes%20part%201.png)
![Task Part 4 - Search Recipes part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%204%20-%20Search%20Recipes%20part%202.png)

Task Part 5 - Update Recipes
![Task Part 5 - Update Recipes part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%205%20-%20Update%20Recipes%20part%201.png)
![Task Part 5 - Update Recipes part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%205%20-%20Update%20Recipes%20part%202.png)
![Task Part 5 - Update Recipes part 3](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%205%20-%20Update%20Recipes%20part%203.png)

Task Part 6 - Delete Recipes
![Task Part 6 - Delete Recipes](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%206%20-%20Delete%20Recipe.png)

Task Part 7 - Quit the App
![Task Part 7 - Quit the App](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.7/images/Task%20Part%207%20-%20Quit%20the%20App.png)

This task encapsulates the application of various Python and SQLAlchemy concepts in a real-world project, showcasing the ability to create a functional and user-friendly command line application.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Screenshots

- Eleven screenshots demonstrating the command-line interface of the task process are included in the repository.

## Summary

In this exercise, the integration of Python with a database using SQLAlchemy, an Object-Relational Mapper, has been explored. The session covered the setup of SQLAlchemy, mapping of Python classes to database tables, and performing CRUD operations in a Pythonic manner. The exercise culminated in the creation of a command line Recipe application, reinforcing the concepts learned and demonstrating the practical application of ORM in software development.
