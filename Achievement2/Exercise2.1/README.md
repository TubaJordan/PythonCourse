# Exercise 2.1: Getting Started with Django

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Web Application Frameworks](#web-application-frameworks)
4. [Your Web Application Framework: Django](#your-web-application-framework-django)
    - [Model View Template (MVT) Architecture](#model-view-template-mvt-architecture)
    - [MVC vs. MVT](#mvc-vs-mvt)
    - [Django Case Study: Flower Shop Web Application](#django-case-study-flower-shop-web-application)
    - [Using Django: Benefits and Drawbacks](#using-django-benefits-and-drawbacks)
5. [Other Popular Python Frameworks](#other-popular-python-frameworks)
6. [Preparing for Installation](#preparing-for-installation)
    - [Python](#python)
    - [Virtual Environment](#virtual-environment)
    - [Visual Studio Code (VSCode)](#visual-studio-code-vscode)
7. [Getting Started with Django](#getting-started-with-django)
    - [Step 1: Create Virtual Environment](#step-1-create-virtual-environment)
        - [On Mac and Linux](#on-mac-and-linux)
        - [On Windows](#on-windows)
    - [Step 2: Install Django](#step-2-install-django)
        - [On Mac](#on-mac)
        - [On Windows](#on-windows-1)
        - [On Linux](#on-linux)
8. [Task](#task)
    - [Task Instructions](#task-instructions)
9. [Learning Journal](#learning-journal)
10. [Summary](#summary)

## Introduction

This exercise introduces Django, a widely-used Python web framework. The focus is on transitioning the Recipe application from a command-line interface to a full-stack web application utilizing Django. Key areas include exploring Django's framework, assessing its advantages and limitations, and executing its installation and configuration.

## Learning Goals

- Explain the differences between Model View Template (MVT) and Model View Controller (MVC) architectures.
- Understand and summarize the benefits and drawbacks of using Django for web development.
- Successfully install Django and set up the development environment.

## Web Application Frameworks

Web application frameworks in JavaScript, like React and Angular, are paralleled in Python with its own set of frameworks. These Python frameworks simplify application development by offering predefined structures for integrating specific application functionalities. They significantly reduce development time by managing complex aspects like database access, template handling, and user-session management.

Such frameworks are integral in constructing both intricate and manageable web applications and pages. Their adoption is widespread among major web companies and platforms, including Instagram, Mozilla, Disqus, Last.fm, and Bitbucket. The preference for web application frameworks in these contexts stems from their rapid deployment capabilities and their contribution to standardized development practices.

## Your Web Application Framework: Django

Django is a "batteries-included" framework, equipped with essential tools and plugins for development, including user-friendly admin panels and authentication features. Its structured approach is beneficial for large-scale project development. Django simplifies web development, allowing focus on project logic. Key attributes of Django include rapid development, secure deployment, and scalability.

Django requires adherence to a specific structure for project development, often referred to as "the Django way." This approach, while initially challenging, becomes more manageable with familiarity. Django's uniqueness primarily stems from its Model View Template (MVT) architecture.

### Model View Template (MVT) Architecture

MVT is a design pattern employed in web application frameworks, offering a reusable solution to common programming challenges. This set of guidelines structures code efficiently.

In contrast to the Model View Controller (MVC) architecture familiar in JavaScript frameworks, Django's MVT architecture has three components:

- **Model**: Manages application data and database functionality, including retrieving, updating, and deleting records.
- **View**: Handles business logic and interfaces between the Model and Template, rendering data on the Template.
- **Template**: Manages the user interface and presentation, structuring output for the browser. Unlike MVC, where the controller code is written by the developer, the Template in MVT handles controller output.

MVT architecture suits applications of various sizes due to its ease of modification and loose coupling of components. It's important to ensure changes in View or Model do not adversely affect the Template.

### MVC vs. MVT

Comparing MVC and MVT:

- MVC involves writing code to fetch data from a database, create presentation layers, map data to URLs, and present it to users.
- MVT in Django automates data fetching and URL mapping, requiring developers to specify only the presentation items.

The following table illustrates the differences between MVC and MVT architectures:

| Feature                                  | MVT (Django)                                 | MVC                              |
|------------------------------------------|----------------------------------------------|----------------------------------|
| **Database**                             | Model                                        | Model                            |
| **Business Logic**                       | View                                         | Controller                       |
| **Presentation**                         | Template                                     | View                             |
| **Control Flow**                         | Managed by Django Framework                  | Managed by the Developer         |
| **Operation Flow for User Requests**     | User → Django → View → Model → View → Template → User (View controls) | User → Controller → Model → Controller → View → Controller → User (View is controlled) |
| **Coupling Between View and Model**      | Loosely coupled (or not coupled)             | Tightly coupled                  |
| **Suitability Based on Application Size**| Suitable for both small and large applications | Generally not suitable for small applications |

### Django Case Study: Flower Shop Web Application

Consider a web application for a flower shop built with Django. The server-side framework handles requests, processes data (flower types, stock, pricing), and generates pages with this content using Python logic. Web pages are then rendered in the client's browser using HTML templates. Django's workflow simplifies the development process, allowing a focus on user experience.

## Using Django: Benefits and Drawbacks

Understanding the appropriate context for using Django involves recognizing its strengths and limitations in different project scenarios.

### Django’s Benefits

- **Python Implementation**: Django's foundation in Python, known for readability and powerful features, supports robust backend development while facilitating feature-rich frontend creation.
- **Rapid Development**: The MVT architecture of Django streamlines the development process, making it efficient and straightforward.
- **High-Speed Processing**: Django enhances application performance, particularly in network transmission and content delivery, due to its efficient architecture.
- **Adherence to DRY Principles**: Emphasizing the DRY (Don't Repeat Yourself) philosophy, Django promotes writing efficient, non-redundant code. This approach is reflected in Django’s modular and reusable project structure.
- **Support for CDNs and Content Management**: Django's capabilities extend to managing Content Delivery Networks, aiding in the streaming of large data volumes, akin to platforms like YouTube and Netflix.
- **Scalability**: The loosely coupled architecture in Django facilitates easy scaling, making it suitable for growing applications.
- **Built-In Security**: With security as a core focus, Django offers secure-by-design features, including automated encryption.
- **Robust Community Support**: As an open-source framework, Django benefits from an extensive community of contributors, offering accessible support and resources.

### Django’s Drawbacks

- **Structured Approach**: Django's stringent structure, while streamlining certain aspects of development, can limit flexibility, requiring adherence to specific methodologies.
- **Not Ideal for Simpler Projects**: Django's comprehensive features may be excessive for simpler projects without database or advanced backend requirements. Its prewritten code base can also be demanding on systems with limited bandwidth.

### When to Use Django

- **For Full-Stack Web Applications**: Django is well-suited for applications with both server-side and client-side components requiring database interaction.
- **Fast Prototyping and High-Speed Applications**: The MVT model and Django's structure make it ideal for rapid prototyping and applications necessitating high-speed performance.
- **Scalable, Secure Large-Scale Systems**: Django's scalability and security features make it a strong candidate for developing large-scale systems.
- **Consideration for Control**: Opting for Django means embracing its structured approach, which might limit control over finer system details. This aspect is crucial when deciding if Django aligns with the project's requirements.

## Other Popular Python Frameworks

While Django is chosen for its robust community support and comprehensive documentation, Python offers a variety of other web application frameworks, each with unique features and use cases.

- **Flask**: A lightweight framework known for its minimalistic approach, Flask provides a straightforward setup for web applications. It is an ideal choice for smaller projects due to its simplicity and less boilerplate code. Flask is favored by companies for projects that don't require the full-scale features of larger frameworks.

- **Pyramid**: Known for its flexibility, Pyramid operates on MVC architecture. It allows more freedom in selecting tools and components, such as database systems and templating engines. This flexibility makes it a choice for developers seeking more control over their application architecture.

- **Web2py**: Inspired by Django, Web2py is another MVC-based framework that stands out for its ease of use, requiring no preliminary installation. It's suitable for rapid development of database-driven applications.

Choosing the appropriate framework depends on specific project needs, such as speed of development, application size, and required levels of security and scalability. The decision also hinges on the level of community and maintenance support available for the framework.

## Preparing for Installation

Prior to starting with Django and developing the first application, the system must be equipped with essential software. These include Python, a virtual environment tool, and a code editor or IDE.

### Python

- **Version Requirement**: Python 3.8.7 is necessary for compatibility with Django. This version should already be installed from previous coursework. If not installed, Python can be downloaded from the official Python website.
- **Installation Reference**: For guidance on installing Python, refer to previous exercises or the official Python documentation.

### Virtual Environment

- **Purpose**: Virtual environments in Python enable isolated development spaces, allowing for clean installations and specific package management.
- **Tool**: The `mkvirtualenv` command, part of the `virtualenvwrapper` package, is used for creating these environments. To verify its installation, use `mkvirtualenv --version` or `virtualenv --version` in the terminal.
- **Upcoming Use**: A new virtual environment will be created for Django development in this course.

### Visual Studio Code (VSCode)

- **Recommended IDE**: VSCode is recommended due to its compatibility and ease of use with Python and Django. However, alternatives like Atom, Sublime Text, or Notepad++ can also be used.
- **Integration**: The course materials are optimized for use with VSCode, aligning with its features and functionalities.

## Getting Started with Django

Installing Django involves creating a virtual environment and then installing Django within it. The process varies slightly across different operating systems.

### Step 1: Create Virtual Environment

#### On Mac and Linux

1. Open Terminal.
2. Create a virtual environment named `web-dev` with the command:

```bash
mkvirtual web-dev
```

This command creates the virtual environment, and any subsequent package installations will be localized to this environment.
3. To deactivate the environment, use `deactivate`. Reactivate it with `workon web-dev`.
4. To remove the virtual environment, use `rmvirtualenv web-dev`, but be cautious as this deletes all files and packages within it.

#### On Windows

1. Open Command Prompt (Note: virtualenvwrapper-win doesn't support PowerShell).
2. Ensure `virtualenvwrapper-win` is installed.
3. Create a new virtual environment `web-dev`:

```bash
mkvirtualenv web-dev
```

This environment is stored in `C:\Users\<username>\Envs`.

### Step 2: Install Django

#### On Mac

1. Activate the virtual environment:

```bash
workon web-dev
```

2. Install Django using pip:

```bash
pip install django
```

3. Verify the Django installation:

```bash
django-admin --version
```

#### On Windows

1. Activate the virtual environment:

```bash
web-dev\Scripts\activate.bat
```

2. Install Django using pip:

```bash
py -m pip install Django
```

3. Verify the Django installation:

```bash
django-admin --version
```

#### On Linux

1. Activate the virtual environment:

```bash
source web-dev/bin/activate
```

2. Install Django using pip:

```bash
pip install django
```

3. Verify the Django installation:

```bash
django-admin --version
```

After completing these steps, Django should be successfully installed in the virtual environment, ready for development.

## Task

### Task Instructions

1. **Create a Text Document**: Prepare a document for writing answers to the following questions. Online research may be necessary to develop informed responses.

2. **Popularity of Django**: Write two to three sentences explaining why Django is popular among web developers
    - Django is popular among web developers due to its simplicity, scalability, and robustness. It follows the "batteries-included" philosophy, offering a wide range of functionalities out-of-the-box, such as an admin panel, user authentication, and database schema migrations. Additionally, its emphasis on reusable components and a clean, pragmatic design makes it easier for developers to build and maintain high-quality web applications efficiently.

3. **Companies Using Django**: Research and list five large companies that use Django, detailing their products or services and how they utilize Django.
   - 1. *Pinterest*: An image sharing and social media service, uses Django to handle vast amounts of content and user interactions.
   - 2. *Instagram*: A social networking service for sharing photos and videos, utilizes Django for its user-friendly interface and ability to scale efficiently.
   - 3. *Mozilla*: Known for the Firefox browser, uses Django for its website and several internal tools.
   - 4. *Spotify*: A music streaming service employs Django to manage complex backend operations and user data processing.
   - 5. *YouTube*: A video sharing platform, leverages Django for certain features and server-side operations.

4. **Scenario Analysis**: For each listed scenario, determine if Django would be an appropriate choice and explain the reasoning:
    - **Multi-user Web Application**:
        - Yes, use Django. It has built-in support for handling user authentication, permissions, and roles, making it ideal for multi-user applications.
    - **Fast Deployment and Ongoing Changes**:
        - Yes, Django is suitable. It’s designed for rapid development and favors convention over configuration, which speeds up development.
    - **Basic Application Without Database or File Operations**:
        - Not ideal for Django. Django is a bit overkill for such simple applications; a lightweight framework or even static site generators might be more appropriate.
    - **Building an Application from Scratch with Full Control**:
        - Yes, but with considerations. Django is very flexible and customizable, but it does have its own way of doing things. For absolute control, a micro-framework might be better.
    - **Large Project with Potential Need for Support**:
        - Yes, Django is ideal. It has a strong community, extensive documentation, and many resources available for support.

5. **Python Installation**:
    - Download and install Python if not already done.
    - Run the command to check the Python version.
    - Include a screenshot of the terminal window showing the command and version in the document.
    ![Python Installation]()

6. **Setting Up a Virtual Environment**:
    - Open a new terminal window and navigate to the desired project folder.
    - Set up and create a virtual environment named `achievement2-practice`.
    - Activate the virtual environment.
    - Include a screenshot of the activated environment in the document.
    ![Setting Up a Virtual Environment]()

7. **Django Installation**:
    - Install Django within the virtual environment.
    - Verify the installation by checking the Django version.
    - Include a screenshot of the terminal with the Django version in the document.
    ![Django Installation]()

8. **Document Export**:
    - Convert the document with all answers and screenshots into a PDF format.
    - PDF Document named `Exercise 2.1 - Task Questions` can be found in this repository.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Summary

This Exercise marks the initial foray into Django, beginning with an overview of web development frameworks. Key focus areas included understanding the Model View Template (MVT) and Model View Controller (MVC) architectures, noting their similarities and differences. The benefits and limitations of Django in various project contexts were also explored, providing insight into when the framework is most effective. The setup process involved preparing the system with essential tools and installing Django in a virtual environment.

The upcoming Exercise will delve into Django's project structure and guide through the creation of the first Django project. The next task in Achievement 2 is set to build upon this foundational knowledge.
