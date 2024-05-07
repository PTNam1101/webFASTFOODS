A simple Django project 

Main feature
  Customer can find item by name and category
  Cart for customer to add item
  Customer profile page to see their order progress and edit their informations
  A discount system based on customer orders
  (give or decrease cutomer point base on orders and it values)
  Higer customer point will have better discount

  Admin page for shop owner to edit, add or remove item from the store

To run the project, first download the code and install following package using pip install:
  asgiref==3.7.2
  Django==4.2.7
  Pillow==10.1.0
  sqlparse==0.4.4
  typing_extensions==4.8.0

Command to start server (make sure you are inside of the project directory):
  cd fastfoodsweb/
  python manage.py runserver

To stop server use: ctrl + C

Connect to server on:
  http://127.0.0.1:8000/

To use admin page, first create super user using this command:
   python manage.py createsuperuser

   enter your user name and password, email is optional

   Adminpage provide ability to edit the database of the project



  
