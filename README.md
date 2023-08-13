# CMS Application using Django REST Framework
This project is a Content Management System (CMS) application developed using Django REST Framework (DRF). It provides APIs for managing users, posts/blogs, and likes.

 # Getting Started
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python (3.x recommended)
pip (Python package manager)
Django (3.x recommended)
Django REST Framework

# Clone the repository to your local machine:
git clone `https://github.com/python-hacked/CMS-Application-using-Django-REST-Framework.git`
cd your-project

# Create a virtual environment (optional but recommended):
`python -m venv venv`
`source venv/bin/activate ` 
`On Windows: venv\Scripts\activate`

# Install project dependencies using requirements.txt:
`pip install -r requirements.txt`

# Apply migrations to create the database schema
`python manage.py makemigrations`
`python manage.py migrate`

# Create a superuser to access the Django admin panel:
`python manage.py createsuperuser`

# Start the development server:
`python manage.py runserver`

Access the admin panel at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.

Access the API endpoints at `http://127.0.0.1:8000/`

# API Endpoints
/users/: List and create users.
/posts/: List, create, read, update, and delete posts. Also provides the number of likes for each post.
/posts/<post_id>/likes/: List likes for a specific post.
/likes/: List and create likes.

