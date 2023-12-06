# Exercise 1.1: Intro to Python Programming

## Table of Contents

1. [Introduction](#introduction)
2. [Benefits of Developing with Python](#benefits-of-developing-with-python)
3. [Installation Instructions](#installation-instructions)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
4. [Setting Up Virtual Environment](#setting-up-virtual-environment)
    - [On Windows](#on-windows)
    - [On macOS/Linux](#on-macoslinux)
5. [Script Creation: add.py](#script-creation-addpy)
6. [IPython Shell Setup](#ipython-shell-setup)
7. [Requirements File](#requirements-file)
8. [GitHub Repository Setup](#github-repository-setup)
9. [Learning Journal](#learning-journal)
10. [Screenshots](#screenshots)
11. [Summary](#summary)

## Introduction

This project is part of the 'Intro to Python Programming' exercise. It includes the installation of Python, the creation and management of a virtual environment, and the use of pip for package management.

## Benefits of Developing with Python

Python is favored for its ease of use, readability, and dynamic typing. It is ideal for backend web development, automating development tasks, and simplifies standard development processes like debugging and documentation.

## Installation Instructions

### Windows

- Check existing Python version: `python --version`.
- [Download Python 3.8.7](https://www.python.org/downloads/release/python-387/) from the official website.
- Follow the installation instructions, ensuring that Python is added to PATH.

### macOS

- Check existing Python installation: `python3 --version`.
- Use the [official installer](https://www.python.org/downloads/release/python-387/) or [Homebrew](https://brew.sh/) to install Python 3.8.7.
- Follow the installation steps for the chosen method.

### Linux

- Check for pre-installed Python: `python3 --version`.
- If necessary, install Python 3.8.7 from source.
- Follow the detailed installation steps for your Linux distribution.

## Setting Up Virtual Environment

### On Windows

1. **Install pip and virtualenvwrapper-win**
   - Install pip (if not installed): Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run `python get-pip.py`.
   - Install virtualenvwrapper-win: `pip install virtualenvwrapper-win`.
2. **Create and Activate a New Environment**
   - Create: `mkvirtualenv cf-python-base`.
   - Activate: `.\cf-python-base\Scripts\activate`.

### On macOS/Linux

1. **Install pip and virtualenvwrapper**
   - Install pip (if not installed): `sudo easy_install pip`.
   - Install virtualenvwrapper: `pip3.8 install virtualenvwrapper`.
   - Add `virtualenvwrapper.sh` to PATH in `.bashrc` or `.zshrc` if not already present.
2. **Configure the Terminal**
   - Add to `.bashrc` or `.zshrc`:
     export VIRTUALENVWRAPPER_PYTHON=$(which python3.8)
     source $(which virtualenvwrapper.sh)

3. **Create and Activate a New Environment**
   - Create: `mkvirtualenv cf-python-base`.
   - Activate: `source cf-python-base/bin/activate`.

## Script Creation: add.py

- The `add.py` script is a simple Python program that adds two numbers input by the user.
- The script prompts the user for two numbers, calculates the sum, and prints the result.

```python
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = a + b

print(c)
```

## IPython Shell Setup

- Install IPython in the virtual environment using pip: `pip install ipython`.
- Launch the IPython shell by simply typing `ipython`.

## Requirements File

- Generate a `requirements.txt` file using the command `pip freeze > requirements.txt`.
- The file lists all packages installed in the environment, ensuring reproducibility.

## GitHub Repository Setup

- The repository is organized with separate folders for each exercise.
- This exercise's materials are located in the `Exercise 1.1` folder.

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- Screenshots demonstrating each step of the process are included in the repository, each appropriately named (e.g., `Step1.png`, `Step2.png`).

## Summary

This exercise covers the basics of setting up Python, understanding its benefits for web development, managing virtual environments, and beginning with Python scripting. It sets the foundation for more advanced topics and projects in the course.
