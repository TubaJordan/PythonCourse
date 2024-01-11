# Exercise 1.6: Databases in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Relational Database Management Systems (RDBMS)](#relational-database-management-systems-rdbms)
   - [Installing MySQL on Ubuntu](#installing-mysql-on-ubuntu)
   - [Installing MySQL on macOS](#installing-mysql-on-macos)
   - [Installing MySQL on Windows](#installing-mysql-on-windows)
4. [Creating a New User in MySQL](#creating-a-new-user-in-mysql)
   - [Accessing MySQL Command Line Client](#accessing-mysql-command-line-client)
   - [Creating a New User](#creating-a-new-user)
   - [Granting Privileges](#granting-privileges)
   - [Exiting MySQL Command Line](#exiting-mysql-command-line)
   - [Connector Installation](#connector-installation)
5. [Installing and Importing the MySQL Connector for Python](#installing-and-importing-the-mysql-connector-for-python)
   - [Installation of MySQL Connector](#installation-of-mysql-connector)
   - [Importing the Connector in Python](#importing-the-connector-in-python)
   - [Connecting to the MySQL Server](#connecting-to-the-mysql-server)
   - [Initializing Cursor Object](#initializing-cursor-object)
6. [Creating a Database](#creating-a-database)
   - [SQL Command to Create a Database](#sql-command-to-create-a-database)
   - [Executing the Command in Python](#executing-the-command-in-python)
   - [Connecting to the Created Database](#connecting-to-the-created-database)
7. [Creating Tables in MySQL](#creating-tables-in-mysql)
   - [Creating a Table](#creating-a-table)
   - [Modifying Tables](#modifying-tables)
   - [Adding Data to a Table](#adding-data-to-a-table)
   - [Automatically Assigning IDs with AUTO_INCREMENT](#automatically-assigning-ids-with-auto_increment)
   - [Displaying Table Contents](#displaying-table-contents)
   - [Updating and Deleting Rows](#updating-and-deleting-rows)
   - [Committing and Closing the Database Connection](#committing-and-closing-the-database-connection)
8. [Task: MySQL Database for Command-Line Recipe App](#task-mysql-database-for-command-line-recipe-app)
   - [Part 1: Create & Connect Database](#part-1-create--connect-database)
   - [Part 2: The Main Menu](#part-2-the-main-menu)
   - [Part 3: Creating a Recipe (create_recipe())](#part-3-creating-a-recipe-create_recipe)
   - [Part 4: Searching for a Recipe (search_recipe())](#part-4-searching-for-a-recipe-search_recipe)
   - [Part 5: Updating a Recipe (update_recipe())](#part-5-updating-a-recipe-update_recipe)
   - [Part 6: Deleting a Recipe (delete_recipe())](#part-6-deleting-a-recipe-delete_recipe)
   - [Part 7: Final Steps](#part-7-final-steps)
9. [Learning Journal](#learning-journal)
10. [Screenshots](#screenshots)
11. [Summary](#summary)

## Introduction

This exercise explores the integration of databases within Python, emphasizing Relational Database Management Systems (RDBMS) through the application of MySQL. The module encompasses the essential skills for database setup and management, as well as the utilization of MySQL in conjunction with Python programming. The fundamental role of databases in efficient data storage and organization is a focal point of the learning experience. Such proficiency is pivotal for the adept handling of databases in the context of web applications, laying a foundational understanding crucial for advanced data management strategies.

Key concepts covered include:

- Establishing and configuring MySQL databases.
- Interfacing Python with MySQL, leveraging the mysql.connector package.
- Understanding the practical significance and applications of databases in systematic data handling.

By the end of this module, learners will acquire the necessary skills to efficiently create, manipulate, and manage databases, thereby enhancing their capability to handle complex data structures within Python-based applications.

## Learning Goals

- Create a MySQL database for your Recipe app.
- Understand the fundamentals of RDBMS and SQL.
- Learn to interact with MySQL databases using Python.

## Relational Database Management Systems (RDBMS)

Relational Database Management Systems (RDBMS) are sophisticated frameworks designed to manage and maintain databases. These systems ensure organized data storage and enhance security through controlled user access. Among various RDBMS options, MySQL is renowned for its extensive use and robust functionality.

In an RDBMS, data is structured in tables, similar to spreadsheets, consisting of rows and columns. Each column within a table is defined with a unique name and a specified data type. Consider a table named 'books', which might include columns such as 'id', 'title', 'author', and 'price'.

Structured Query Language (SQL) is utilized for interacting with databases. SQL commands are designed to be straightforward and user-friendly. For instance, to insert a new entry into the 'books' table, one might use a command like:

```sql
INSERT INTO books (id, title, author, price) VALUES (101, '1984', 'George Orwell', 15.99);
```

This command would add a new book, "1984" by George Orwell, priced at $15.99, into the 'books' table.

To facilitate the execution of SQL commands via Python, a connection is established between the Python environment and the RDBMS using a connector package. Each RDBMS has a specific connector for this purpose.

For example, connecting to a MySQL database using Python might involve the following steps:

```python
import mysql.connector

# Establishing a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Creating a cursor object to interact with the database
cursor = conn.cursor()

# Executing an SQL command to insert data
cursor.execute("INSERT INTO books (id, title, author, price) VALUES (101, '1984', 'George Orwell', 15.99);")

# Committing the changes to the database
conn.commit()

# Closing the cursor and connection to clean up
cursor.close()
conn.close()
```

In this example, the MySQL connector is used to establish a connection, a cursor is created to execute SQL commands, and the changes are committed to the database. Finally, the cursor and connection are closed to ensure a clean exit.

Before leveraging the connector for database interaction, it's imperative to have MySQL Server installed and appropriately configured on the system. This installation is a prerequisite for integrating MySQL functionalities into Python applications.

### Installing MySQL on Ubuntu

### Step-by-Step Installation Process

1. **Open Terminal**: Use `Ctrl + Alt + T` to open the terminal.
2. **Update Packages**: Run `sudo apt update && sudo apt upgrade` to update your package lists and upgrade your packages.
3. **Install MySQL Server**: Execute `sudo apt install mysql-server`. The installation duration may vary.
4. **Configure MySQL Security**: Run `sudo mysql_secure_installation`. This step involves several Yes/No prompts:
   - **Password Validation**: Opt for simple setup without password validation.
   - **Root Password**: Set a memorable password for the root user.
   - **Anonymous Users**: Allow anonymous users for testing purposes.
   - **Remote Root Login**: Disallow remote root user login.
   - **Test Database**: Keep the test database.
   - **Privilege Tables**: Refresh privilege tables to apply changes.
5. **Verify Installation**: Use `sudo systemctl status mysql.service` to check if MySQL is active. Exit the status display using `Ctrl + C`.

### Example Ubuntu

```bash
sudo apt update && sudo apt upgrade
sudo apt install mysql-server
sudo mysql_secure_installation
sudo systemctl status mysql.service
```

### Installing MySQL on macOS

### Installation Steps

1. **Download MySQL**: Visit MySQL Community Downloads and download the DMG Archive for macOS.
2. **Skip Oracle Account**: Bypass the Oracle account setup with the “No thanks, just start my download” link.
3. **Open Installer**: If there's an error, open Spotlight Search (`Cmd + Spacebar`), search for "Security & Privacy", and allow the MySQL installer.
4. **Run Installer**: Follow the on-screen instructions and select 'Use Strong Password Encryption'.
5. **Configure Root User**: Choose a password for the root user and ensure MySQL Server starts post-installation.

### Verification

Open Spotlight Search, find "Preferences", and look for MySQL to verify if the server is active.

### Example macOS

```bash
# Assuming MySQL DMG file is downloaded
# Open the installer and follow on-screen instructions
# Configure the settings as per the steps
```

### Installing MySQL on Windows

### Installation Guide

1. **Download MySQL**: Navigate to MySQL Community Downloads, select Windows OS, and download the MSI installer.
2. **Skip Oracle Accoun**t: Choose “No thanks, just start my download”.
3. **Installer Setup**: Run the installer and select 'Developer Default'.
4. **Configuration Steps**:
    - Leave Type and Network options unchanged.
    - Choose 'Strong Password Encryption'.
    - Set a root password.
    - Configure Windows Service settings as recommended.
    - Connect to the server using the set root password.

### Completing Installation

Follow the installer's prompts to complete the MySQL setup.

```bash
# Download and run the MySQL MSI installer
# Follow the setup wizard, choosing 'Developer Default' and configuring as per the steps
```

## Creating a New User in MySQL

Creating a dedicated user for accessing the MySQL server is an important step for managing permissions and ensuring secure database interactions, particularly when interfacing with Python scripts.

### Accessing MySQL Command Line Client

On Ubuntu

1. Open a terminal.
2. Enter `sudo mysql` to launch the MySQL command line client.

On macOS

1. Open a terminal.
2. Navigate to the MySQL installation directory: `cd /usr/local/mysql/bin`.
3. Launch the MySQL client: `./mysql -u root -p` and enter the root password when prompted.

On Windows

1. Go to the Start menu.
2. Open the MySQL section and launch the MySQL Command Line Client.
3. Enter the root user's password to access the prompt.

### Creating a New User

Once in the MySQL command line interface, create a new user by executing SQL commands directly.

SQL Command to Create a New User
Create a user named `cf-python` with a specified password. This user is designated for local access (`localhost`).

```sql
CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';
```

### Granting Privileges

New users have no permissions by default. To enable them to perform database operations:

SQL Command to Grant Privileges
Grant the user `cf-python` all privileges for all databases and tables using the wildcard `*.*`.

```sql
GRANT ALL PRIVILEGES ON *.* TO 'cf-python'@'localhost';
```

*Note*
The `*.*` syntax is a wildcard representing all databases and tables. It can be replaced with specific database and table names to tailor user access.

### Exiting MySQL Command Line

After setting up the user and adjusting privileges, type `exit` to leave the MySQL command line interface.

### Connector Installation

With the MySQL database configured and the user established, the next step is to install the MySQL connector package in Python. This package enables Python scripts to communicate with the MySQL server.

Installing MySQL Connector in Python
Use pip to install the MySQL connector package, which establishes a bridge between Python scripts and the MySQL database.

```bash
pip install mysql-connector-python
```

This command installs the necessary connector, allowing Python to interact with MySQL using the newly created user credentials.

## Installing and Importing the MySQL Connector for Python

To enable Python scripts to interact with a MySQL database, installing the MySQL Connector package is essential. This package serves as a bridge between Python and MySQL, facilitating database operations within a Python environment.

### Installation of MySQL Connector

1. **Open a Terminal**: Access your terminal or command line interface.
2. **Activate Virtual Environment (Optional)**: If using a virtual environment, activate it.
3. **Install MySQL Connector**: Use pip to install the `mysql-connector-python` package.

```bash
pip install mysql-connector-python
```

#### Important Note

Ensure to execute these commands within an IPython shell for this exercise. Regular Python shells or script files might not retain changes made during the session.

### Importing the Connector in Python

After installation, the next step is to import the connector in your Python environment:

```python
import mysql.connector
```

### Connecting to the MySQL Server

Establish a connection to the MySQL server using the `mysql.connector.connect()` method. This method requires specific arguments to define the connection parameters.

Connection Syntax

```python
conn = mysql.connector.connect(
    host="<hostname>",
    user="<username>",
    passwd="<password>"
)
```

- **host**: The hostname of the MySQL server. Use `localhost` for local server access.
- **user**: The username for logging into MySQL. For initial setup, this is usually the root user or a user created specifically for Python scripts.
- **passwd**: The password associated with the user account.

Example Connection

```python
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)
```

In this example, `conn` is the connection object that links the Python session to the MySQL server.

### Initializing Cursor Object

Create a cursor object from the connection to execute SQL queries:

```python
cursor = conn.cursor()
```

The cursor object is a crucial tool for performing database operations like creating databases, adding data, and querying information.

### Visual Representation

The connection process can be visualized as Python sending requests through the connector to the MySQL server, and receiving responses back through the same channel. This interaction is crucial for database manipulation in Python applications.

## Creating a Database

Creating a database in MySQL involves executing SQL commands through a Python script. This process enables the structuring of data in an organized and efficient manner, essential for robust data management.

### SQL Command to Create a Database

To create a database, use the SQL command `CREATE DATABASE` followed by the desired database name.

SQL Syntax

```sql
CREATE DATABASE <database name>;
```

### Executing the Command in Python

In Python, the cursor object, derived from the MySQL connection, is used to execute SQL commands.

Python Syntax for Executing SQL Command

```python
cursor.execute("<SQL query>")
```

Example: Creating a New Database

```python
cursor.execute("CREATE DATABASE my_database")
```

This command creates a new database named `my_database`.

### Connecting to the Created Database

After creating the database, the next step is to switch to it in order to perform further operations like creating tables or inserting data.

SQL Command to Use a Database

```sql
USE <database name>;
```

Executing the Use Command in Python

```python
cursor.execute("USE my_database")
```

This command sets `my_database` as the active database for subsequent operations.

### Ready to Use

With these steps, the database `my_database` is now ready for data storage and manipulation. This process forms the foundational step in database management within a Python environment, allowing for the structured organization of data and efficient retrieval and updating of information as needed.

## Creating Tables in MySQL

To effectively store and manage data in MySQL, creating structured tables is a fundamental step. This section covers the essentials of creating tables and performing basic table operations using SQL commands within a Python environment.

### Creating a Table

The standard SQL query to create a table involves defining its columns and their respective data types.

SQL Syntax for Table Creation

```sql
CREATE TABLE <table name> (
    <column 1 name> <data type for column 1>,
    <column 2 name> <data type for column 2>,
    ...
    <column N name> <data type for column N>
)
```

Common Data Types in MySQL

- `VARCHAR(n)`: A string with a variable length, where n is the maximum number of characters.
- `INT`: For integers.
- `FLOAT`: For floating-point numbers.
- `DATETIME`: For date and time values.

Example: Creating an Inventory Table

```python
cursor.execute("""
CREATE TABLE inventory (
    item_id INT,
    item_name VARCHAR(50),
    price FLOAT,
    quantity INT
)
""")
```

In this example, an `inventory` table is created with four columns: `item_id`, `item_name`, `price`, and `quantity`.

### Modifying Tables

The `ALTER TABLE` statement allows for various modifications to an existing table, such as renaming it, changing column names, or adding new columns.

Renaming a Table

```python
cursor.execute("ALTER TABLE inventory RENAME TO stock")
```

Renaming a Column

```python
cursor.execute("ALTER TABLE stock RENAME COLUMN qty TO quantity")
```

Adding a New Column

```python
cursor.execute("ALTER TABLE stock ADD COLUMN manufacturer_name TEXT")
```

Viewing Table Structure

Use the `DESCRIBE` command to view the structure and column details of a table.

```python
cursor.execute("DESCRIBE stock")
result = cursor.fetchall()
for row in result:
    print(row)
```

### Adding Data to a Table

To insert data into a table, use the `INSERT INTO` statement.

Example: Adding a New Entry

```python
cursor.execute("""
INSERT INTO stock (item_name, manufacturer_name, price, quantity)
VALUES ('Water', 'Aquafina', 10.00, 20)
""")
```

Using Placeholders for Data Insertion

```python
sql = "INSERT INTO stock (item_id, item_name, price, quantity, manufacturer_name) VALUES (%s, %s, %s, %s, %s)"
val = (2, 'Coca-Cola', 2.5, 30, 'The Coca-Cola Company')
cursor.execute(sql, val)
```

### Automatically Assigning IDs with AUTO_INCREMENT

To auto-generate unique IDs for new rows, use the `AUTO_INCREMENT` attribute in the primary key column.

Example: Enabling AUTO_INCREMENT

```python
cursor.execute("ALTER TABLE stock MODIFY COLUMN item_id INT PRIMARY KEY AUTO_INCREMENT")
```

### Displaying Table Contents

Use the `SELECT` query to display data from a table.

Displaying Specific Columns

```python
cursor.execute("SELECT item_id, item_name, manufacturer_name, price, quantity FROM stock")
```

Displaying All Columns

```python
cursor.execute("SELECT * FROM stock")
```

### Updating and Deleting Rows

Updating a Row

```python
cursor.execute("UPDATE stock SET price = 35 WHERE item_id = 3")
```

Deleting a Row

```python
cursor.execute("DELETE FROM stock WHERE item_id = 5")
```

### Committing and Closing the Database Connection

After performing operations, commit the changes and close the database connection.

```python
conn.commit()
conn.close()
```

### Note on Using SQLite

For simpler databases or testing purposes, SQLite can be a more convenient choice. SQLite does not require a server setup and stores data in .db files, which can be directly accessed by applications like Python.

These steps and examples provide a comprehensive guide to creating and manipulating tables in MySQL using Python. The ability to create, modify, and interact with tables is crucial for effective data management in relational databases.

## Task: MySQL Database for Command-Line Recipe App

This task entails enhancing a command-line Recipe application by integrating MySQL database operations. The app will perform CRUD (Create, Read, Update, Delete) operations on recipes stored in a MySQL database.

### Part 1: Create & Connect Database

- **Import MySQL Connector**: Include the `mysql.connector` module in your script.
- **Initialize Connection**: Create a connection object `conn` with parameters (hostname: `localhost`, username: `cf-python`, password: `password`).
- **Initialize Cursor**: Create a cursor object from the connection to execute SQL queries.
- **Create Database**: Use `CREATE DATABASE IF NOT EXISTS task_database` to ensure uniqueness.
- **Select Database**: Switch to the newly created database with `USE task_database`.
- **Create Table**: Define a `Recipes` table with columns for `id`, `name`, `ingredients`, `cooking_time`, and `difficulty`. Ensure id increments automatically and is set as the primary key.

```python
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "cf-python",
    passwd = "password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
)''')
```

### Part 2: The Main Menu

- Develop a main menu function `main_menu()` that allows users to choose from creating, searching, updating, or deleting recipes.
- Implement a loop to facilitate continuous user interaction until an exit condition is met.
- Define functions for each menu option that accept `conn` and `cursor` as arguments.

```python
def main_menu(conn, cursor):
    choice = ""
    while(choice != "quit"):

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
        print("2. Search for recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe\n")
        print("Type 'quit' to exit the program\n")
        choice = input("Your choice: ").strip().lower()
        print()


        if choice in ["1", "2", "3", "4"]:

            if choice == "1":
                create_recipe(conn, cursor)
            elif choice == "2":
                search_recipe(conn, cursor)
            elif choice == "3":
                update_recipe(conn, cursor)
            elif choice == "4":
                delete_recipe(conn, cursor)
        elif choice == "quit":
            print("=============================================")
            print("      Thanks for using the Recipe App!       ")
            print("             See you next time               ")
            print("=============================================")
            break
        else:
            print("---------------------------------------------------")
            print("Invalid choice! Please enter 1, 2, 3, 4, or 'quit'.")
            print("---------------------------------------------------\n")
            print("...returning to main menu\n\n")

    conn.close()
```

### Part 3: Creating a Recipe (`create_recipe()`)

- Collect recipe details (name, cooking_time, ingredients as a string list).
- Implement `calculate_difficulty()` to determine the recipe's difficulty based on cooking time and ingredients.
- Convert ingredients list to a comma-separated string using `join()`.
- Construct and execute an INSERT SQL query to add the recipe to the database.
- Commit changes to the database.

```python
def create_recipe(conn, cursor):
    print()
    print("==================================================")
    print("           *** Create New Recipes ***             ")
    print("==================================================")
    print("Please follow the steps below to add new recipes!\n")
    
    while True:
        try:
            number_of_recipes = int(input("How many recipes would you like to enter? "))
            if number_of_recipes < 1:
                print("Please enter a positive number.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    for i in range(number_of_recipes):
        print(f"\nEnter recipe #{i + 1}")
        print("---------------------")

        name = input("  Enter the recipe name: ")
        cooking_time = int(input("  Enter the cooking time in minutes: "))
        ingredients_input = input("  Enter the recipe's ingredients, separated by a comma: ")
        ingredients = ingredients_input.split(", ")

        difficulty = calculate_difficulty(cooking_time, ingredients)

        ingredients_str = ", ".join(ingredients)

        try:
            insert_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (name, ingredients_str, cooking_time, difficulty))
            conn.commit()

            print("  ** Recipe successfully added! **")
        except mysql.connector.Error as err:
            print("Error occurred: ", err)
    
    final_message = "Recipe successfully added!" if number_of_recipes == 1 else "All recipes successfully added!"

    print()
    print("--------------------------------------------------")
    print(f"            {final_message}            ")
    print("--------------------------------------------------\n")
    print("...returning to main menu\n\n")


def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        return "Hard"
```

### Part 4: Searching for a Recipe (`search_recipe()`)

- Retrieve a list of all ingredients from the database.
- Display ingredients and allow user to select one for searching.
- Build a SELECT SQL query using LIKE operator and wildcard `%` to find recipes containing the chosen ingredient.
- Execute the query and display the results.

```python
def format_recipe_display(recipe):
    print(f"\nRecipe: {recipe[1].title()}")
    print(f"  Time: {recipe[3]} mins")
    print("  Ingredients:")
    for ingredient in recipe[2].split(", "):
        print(f"  - {ingredient.title()}")
    print(f"  Difficulty: {recipe[4]}")        


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("***************************************************************")
        print("        There are no recipes in the database to search.        ")
        print("                  Please create a new recipe!                  ")
        print("***************************************************************\n")
        print("...returning to main menu\n\n")
        return

    all_ingredients = set()

    print()
    print("=================================================================")
    print("           *** Search for a Recipe By Ingredient ***             ")
    print("=================================================================")
    print("Please enter a number to see all recipes that use that ingredient\n")

    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient.strip())

    for i, ingredient in enumerate(sorted(all_ingredients)):
        print(f"{i+1}.) {ingredient.title()}")

    print()
    while True:
        try:
            choice = int(input("Enter a number for the ingredient: "))
            if 1 <= choice <= len(all_ingredients):
                break
            else:
                print()
                print("Please enter a number within the list range.\n")
        except ValueError:
            print()
            print("Invalid input. Please enter a number.\n")

    selected_ingredient = sorted(all_ingredients)[choice - 1]

    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(search_query, ("%" + selected_ingredient + "%",))
    search_results = cursor.fetchall()

    if search_results:
        recipe_count = len(search_results)
        recipe_word = "recipe" if recipe_count == 1 else "recipes"
        print(f"\n{recipe_count} {recipe_word} found containing '{selected_ingredient.title()}'\n")
        for recipe in search_results:
            format_recipe_display(recipe)

        print()
        print("--------------------------------------------------")
        print("            Recipe search successful!             ")
        print("--------------------------------------------------\n")
        print("...returning to main menu\n")
    else:
        print(f"No recipes found containing '{selected_ingredient.title()}'\n")
    
    print("\n")
```

### Part 5: Updating a Recipe (`update_recipe()`)

- Fetch and display all recipes from the database.
- Allow the user to select a recipe and the specific column (name, cooking_time, ingredients) to update.
- If cooking_time or ingredients are updated, recalculate the difficulty.
- Execute the UPDATE SQL query and commit changes.

```python
def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("***************************************************************")
        print("        There are no recipes in the database to update.        ")
        print("                  Please create a new recipe!                  ")
        print("***************************************************************\n")
        print("...returning to main menu\n\n")
        return
    
    print()
    print("=================================================================")
    print("             *** Update a Recipe By ID Number ***                ")
    print("=================================================================")
    print("Please enter an ID number to update that recipe\n")


    print("---- Avaiable Recipes ----\n")
    for result in results:
        ingredients_list = result[2].split(", ")
        capitalized_ingredients = [ingredient.title() for ingredient in ingredients_list]
        capitalized_ingredients_str = ", ".join(capitalized_ingredients)

        print(f"ID: {result[0]} | Name: {result[1]}")
        print(f"Ingredients: {capitalized_ingredients_str} | Cooking Time: {result[3]} | Difficulty: {result[4]}\n")

    while True:
        try:
            print()
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            print()

            cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (recipe_id,))
            if cursor.fetchone()[0] == 0:
                print("No recipe found with the entered ID. Please try again.\n")
            else:
                break
        except ValueError:
            print()
            print("Invalid input. Please enter a numeric value.\n")

    selected_recipe = next((recipe for recipe in results if recipe[0] == recipe_id), None)
    if selected_recipe:
        print(f"Which field would you like to update for '{selected_recipe[1]}'?")
    else:
        print("Recipe not found.")
        return
    print(" - Name")
    print(" - Cooking Time")
    print(" - Ingredients\n")

    update_field = input("Enter your choice: ").lower()
    print()

    if update_field == "cooking time":
        update_field = "cooking_time"

    if update_field not in ["name", "cooking_time", "ingredients"]:
        print("Invalid field. Please enter 'name', 'cooking_time', or 'ingredients'.")
        return
    
    if update_field == "cooking_time" or update_field == "cooking time":
        while True:
            try:
                new_value = int(input("Enter the new cooking time (in minutes): "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for cooking time.")
    else:
        new_value = input(f"Enter the new value for {update_field}: ")

    update_query = f"UPDATE Recipes SET {update_field} = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, recipe_id))

    if update_field in ["cooking_time", "ingredients"]:
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        updated_recipe = cursor.fetchone()
        new_difficulty = calculate_difficulty(int(updated_recipe[0]), updated_recipe[1].split(", "))

        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))

    conn.commit()

    print()
    print("--------------------------------------------------")
    print("           Recipe successfully updated!           ")
    print("--------------------------------------------------\n")
    print("...returning to main menu\n\n")

```

### Part 6: Deleting a Recipe (`delete_recipe()`)

- Display all recipes and allow the user to choose one for deletion by its id.
- Use the DELETE SQL statement to remove the selected recipe from the database.
- Commit the changes.

```python
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("***************************************************************")
        print("        There are no recipes in the database to delete.        ")
        print("                  Please create a new recipe!                  ")
        print("***************************************************************\n")
        print("...returning to main menu\n\n")
        return
    
    print()
    print("=================================================================")
    print("             *** Delete a Recipe By ID Number ***                ")
    print("=================================================================")
    print("Please enter the ID number of the recipe to remove")
    print("*Note: This can NOT be undone\n")

    
    print("---- Avaiable Recipes ----\n")
    for result in results:
        ingredients_list = result[2].split(", ")
        capitalized_ingredients = [ingredient.title() for ingredient in ingredients_list]
        capitalized_ingredients_str = ", ".join(capitalized_ingredients)

        print(f"ID: {result[0]} | Name: {result[1]}")
        print(f"Ingredients: {capitalized_ingredients_str} | Cooking Time: {result[3]} | Difficulty: {result[4]}\n")

    while True:
        try:
            recipe_id = int(input("Enter the ID of the recipe to delete: "))
            print()

            cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (recipe_id,))
            if cursor.fetchone()[0] == 0:
                print("No recipe found with the entered ID. Please try again.\n")
            else:
                
                cursor.execute("SELECT name FROM Recipes WHERE id = %s", (recipe_id,))
                recipe_name = cursor.fetchone()[0]
                confirm = input(f"Are you sure you want to delete '{recipe_name}'? (Yes/No): ").lower()
                
                if confirm == "yes":
                    break
                elif confirm == "no":
                    print()
                    print("Deletion cancelled. Returning to main menu\n\n")
                    return
                else:
                    print()
                    print("Please answer with 'Yes' or 'No'.\n")
                
        except ValueError:
            print()
            print("Invalid input. Please enter a numeric value.\n")

    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))

    conn.commit()

    print()
    print("--------------------------------------------------")
    print("           Recipe successfully deleted!           ")
    print("--------------------------------------------------\n")
    print("...returning to main menu\n\n")
```

### Part 7: Final Steps

1. Initial Setup and Script Execution

- Save the Python script for your Recipe app.
- Ensure the MySQL server is operational.
- Execute the script to start interacting with your database.

2. Creating Recipes

- Task Description: Use the option to create 3 to 4 recipes in the application.
- Process: Select the 'Create a Recipe' option and input the necessary details for each recipe.
- Screenshots:
![Create Recipe - Part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Create%20Recipe%20-%20part%201.png)
![Create Recipe - Part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Create%20Recipe%20-%20part%202.png)

3. Searching for Recipes

- Task Description: Search for recipes based on a specific ingredient.
- Process: Choose the 'Search for a Recipe' option and select an ingredient to filter recipes.
- Screenshots:
![Search for a Recipe - Part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Search%20for%20a%20Recipe%20-%20part%201.png)
![Search for a Recipe - Part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Search%20for%20a%20Recipe%20-%20part%202.png)

4. Updating Recipes

- Task Description: Modify details in existing recipes.
- Process: Select the 'Update a Recipe' option and make changes to 2 or 3 recipes.
- Screenshots:
![Recipe Update - Part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Recipe%20Update%20-%20part%201.png)
![Recipe Update - Part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Recipe%20Update%20-%20part%202.png)
![Recipe Update - Part 3](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Recipe%20Update%20-%20part%203.png)
![Recipe Update - Part 4](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Recipe%20Update%20-%20part%204.png)

5. Deleting Recipes

- Task Description: Remove a recipe from the database.
- Process: Use the 'Delete a Recipe' option to eliminate a chosen recipe.
- Screenshots:
![Delete a Recipe - Part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Delete%20a%20Recipe%20-%20part%201.png)
![Delete a Recipe - Part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Delete%20a%20Recipe%20-%20part%202.png)

6. Exiting the Application

- Task Description: Conclude the session with the application.
- Process: Use the designated exit keyword (e.g., 'quit') to close the application.
- Screenshots:
![Quit the Program](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.6/images/Quitting%20the%20Program.png)

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- Eleven screenshots demonstrating the command-line interface of the task process are included in the repository.

## Summary

This exercise focuses on integrating Python with MySQL, a widely-used Relational Database Management System (RDBMS). It covers the installation of MySQL across various operating systems and the creation of new MySQL users. The exercise involves linking Python to MySQL through a connector package and utilizing SQL queries for creating and managing databases and tables. Key skills developed include executing SQL queries via Python, manipulating table data, and managing database operations. This exercise provides essential skills for advanced data management and web framework applications.
