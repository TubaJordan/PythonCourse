# Exercise 1.6: Databases in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Relational Database Management Systems (RDBMS)](#relational-database-management-systems-rdbms)
4. [Setting Up MySQL](#setting-up-mysql)
   - [Installation on Different Operating Systems](#installation-on-different-operating-systems)
   - [Creating a New User in MySQL](#creating-a-new-user-in-mysql)
5. [MySQL Connector for Python](#mysql-connector-for-python)
   - [Installation and Import](#installation-and-import)
   - [Connecting to MySQL Server](#connecting-to-mysql-server)
6. [Creating and Managing a Database](#creating-and-managing-a-database)
   - [Creating a Database and Tables](#creating-a-database-and-tables)
   - [The ALTER TABLE Statement](#the-alter-table-statement)
7. [Interacting with the Database](#interacting-with-the-database)
   - [Adding Entries](#adding-entries)
   - [Displaying Table Contents](#displaying-table-contents)
   - [Updating and Deleting Rows](#updating-and-deleting-rows)
8. [Committing Changes and Closing Connection](#committing-changes-and-closing-connection)
9. [Task: MySQL for Recipe App](#task-mysql-for-recipe-app)
   - [Overview](#overview)
   - [Part 1: Create & Connect Database](#part-1-create--connect-database)
   - [Part 2: The Main Menu](#part-2-the-main-menu)
   - [Part 3: Creating a Recipe](#part-3-creating-a-recipe)
   - [Part 4: Searching for a Recipe](#part-4-searching-for-a-recipe)
   - [Part 5: Updating a Recipe](#part-5-updating-a-recipe)
   - [Part 6: Deleting a Recipe](#part-6-deleting-a-recipe)
   - [Part 7: Final Steps](#part-7-final-steps)
10. [Summary](#summary)
11. [Resources](#resources)

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

## Setting Up MySQL

### Installation on Different Operating Systems

Installation procedures vary based on the operating system (Ubuntu, macOS, Windows). Follow the specific instructions provided to install MySQL on your system and ensure it's correctly set up and running.

### Creating a New User in MySQL

Learn how to create a new user in MySQL and assign necessary privileges. This step is crucial for securely accessing and managing your databases.

## MySQL Connector for Python

### Installation and Import

#### Installing MySQL on Ubuntu

##### Step-by-Step Installation Process

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

###### Example

```bash
sudo apt update && sudo apt upgrade
sudo apt install mysql-server
sudo mysql_secure_installation
sudo systemctl status mysql.service
```

### Connecting to MySQL Server

Understand how to initialize a connection to the MySQL server using the connector, and create a cursor object to execute SQL queries from Python.

## Creating and Managing a Database

### Creating a Database and Tables

Learn to create a new database and tables within it, using SQL queries executed from Python. Understand the importance of structuring your data with the appropriate columns and data types.

### The ALTER TABLE Statement

Explore various operations that can be performed on tables, such as renaming a table, changing column names, adding new columns, and more, using the ALTER TABLE statement.

## Interacting with the Database

### Adding Entries

Add new data entries to your tables and understand the significance of each SQL query used for this purpose.

### Displaying Table Contents

Learn how to retrieve and display data from your tables using SELECT queries.

### Updating and Deleting Rows

Update and delete specific rows in your tables based on certain conditions using UPDATE and DELETE statements.

## Committing Changes and Closing Connection

Understand the importance of committing your changes to the database and properly closing the connection once your operations are complete.

## Task: MySQL for Recipe App
