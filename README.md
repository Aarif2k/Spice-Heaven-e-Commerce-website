# Spice-Heaven-e-Commerce-website

Overview
Spice Heaven is a fully functional e-commerce website built with Django, designed for selling a variety of spices. The website features a user-friendly interface for browsing products. It also includes an admin panel for managing products and categories.

Features
User Authentication: Sign up, login, logout.
Product Management: Add, update, delete, and view product details.
Shopping Cart: Users can add, update, and remove items from the cart.
Responsive Design: Optimized for both desktop and mobile devices.

Technologies Used
Backend:
Django: Web framework used to build the core of the website.
MySQL: Database for storing all data related to products, users, etc.
Frontend:
HTML, CSS, JavaScript: Standard web technologies.
Bootstrap: For responsive and mobile-first design.
Django Crispy Forms: For better form rendering.
Other Tools:
Pillow: Image processing library used for managing product images.

Installation
Prerequisites
asgiref==3.8.1
Django==5.0.6
sqlparse==0.5.0
tzdata==2024.1
Virtual Environment (optional but recommended)
Setup Instructions
Clone the Repository:

git clone https://github.com/Aarif2k/Spice-Heaven-e-Commerce-website.git
cd spice-heaven
Create and Activate a Virtual Environment:

python -m venv venv
venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Configure Database:

Update the DATABASES setting in settings.py with your MySQL database credentials.
Apply migrations:
python manage.py migrate

Run the Development Server:
python manage.py runserver

Create a Superuser:
python manage.py createsuperuser

Access the Website:
Open your web browser and go to http://127.0.0.1:8000/ to view the website.

Usage
Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created. Here, you can manage products.
