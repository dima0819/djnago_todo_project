Django To-Do List Project

A simple To-Do List web application built with Django. This project was created to practice the fundamentals of the Django framework, focusing on the MVT (Model-View-Template) architecture and full CRUD (Create, Read, Update, Delete) functionality.

Features

Create: Add new tasks to the list.

Read: View all tasks in a list and see details for a specific task.

Update: Edit existing tasks (e.g., change the title, description, or mark as complete) using UpdateView.

Delete: Remove tasks from the list using DeleteView.

Admin Panel: Full admin integration to manage Task objects directly via the Django admin site.

Technology Stack

Backend: Django

Language: Python

Database: SQLite (default Django database)

Getting Started: Running Locally

Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Python 3.8+

Git

Installation

Clone the repository:

git clone [https://github.com/dima0819/djnago_todo_project.git](https://github.com/dima0819/djnago_todo_project.git)
cd djnago_todo_project


Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


Install dependencies:
(This project's main dependency is Django)

pip install Django


Apply database migrations:
This will create the db.sqlite3 file and the necessary database tables.

python manage.py migrate


Run the development server:

python manage.py runserver


The application will be available at http://127.0.0.1:8000/.

(Optional) Create a superuser:
To access the admin panel (/admin) and manage tasks:

python manage.py createsuperuser


Follow the prompts to create your admin account.

