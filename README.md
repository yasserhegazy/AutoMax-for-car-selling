# AutoMax

A Django-based web application for buying and selling cars.

## What it does

AutoMax is a feature-rich web application that simulates a real-world car marketplace. It allows users to not only browse a catalog of cars but also to actively participate in the marketplace. Users can register for an account, log in, and manage their own profile. The core functionality revolves around car listings, which users can create to sell their vehicles. These listings include detailed information such as the car's make, model, year, mileage, and photos. Other users can then view these listings, filter them based on their preferences, and even "like" them to save them for later. The application also includes a feature to contact the seller of a car via email.

## How it works

The application is built using the Model-View-Template (MVT) design pattern, which is the core of the Django framework.

*   **Models**: The data structure of the application is defined in the `models.py` files of the `main` and `users` apps. These models (e.g., `Listing`, `User`, `Profile`, `LikedListing`) are mapped to database tables.
*   **Views**: The `views.py` files contain the business logic of the application. They handle user requests, interact with the models to retrieve or save data, and then render the appropriate templates.
*   **Templates**: The HTML files in the `templates` directory are responsible for the presentation layer. They receive data from the views and display it to the user. The templates use Django's templating language to dynamically generate HTML.
*   **Forms**: Django forms are used to handle user input for creating and editing listings and profiles. The application uses `django-crispy-forms` to render these forms with Bootstrap 5 styling.
*   **Static Files**: CSS, JavaScript, and images are managed as static files.
*   **Routing**: The `urls.py` files map URLs to specific views, directing the flow of the application.

## Knowledge Needed

To build a project like AutoMax, you would need a good understanding of the following concepts and technologies:

*   **Python**: The core programming language for Django.
*   **Django**: A strong grasp of the Django framework is essential, including:
    *   Models and the ORM (Object-Relational Mapper)
    *   Views (both function-based and class-based)
    *   Templates and the Django Template Language
    *   Forms (including `ModelForm`)
    *   User authentication and authorization
    *   URL routing
    *   Static and media file management
*   **HTML, CSS, and JavaScript**: For building the user interface.
*   **Bootstrap 5**: For responsive and modern styling.
*   **jQuery**: For client-side scripting and AJAX requests (like the "like" feature).
*   **Database Concepts**: Understanding of relational databases and how to model data.
*   **Git and GitHub**: For version control and collaboration.
*   **Virtual Environments**: For managing project dependencies.

## Features

*   User registration and authentication
*   Create, edit, and delete car listings
*   Browse and filter car listings
*   Like and unlike listings
*   User profiles with a list of their listings and liked listings

## Technologies Used

*   Django
*   Bootstrap 5
*   jQuery
*   SQLite

## Setup and Installation

1.  **Clone the repository:**

    ```
    git clone <repository-url>
    ```

2.  **Create and activate a virtual environment:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```
    pip install -r requirements.txt
    ```

4.  **Run the database migrations:**

    ```
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```
    python manage.py runserver
    ```