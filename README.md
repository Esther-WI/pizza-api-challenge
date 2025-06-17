#  Pizza API Challenge

A RESTful API built with Flask to manage Restaurants, Pizzas, and their relationships using SQLAlchemy and Flask-Migrate.

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd pizza-api-challenge

2. **Create a virtual environment and install dependencies**
pipenv install
pipenv shell

3 **Run the development server**
flask run

### Database Migration & Seeding Instructions
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py

#### Route Summary
Method	/Route	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<int:id>	Get one restaurant & its pizzas
DELETE	/restaurants/<int:id>	Delete a restaurant
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Create a new RestaurantPizza

##### Example Requests & Responses
GET /restaurants
Response:

json
Copy code
[
  {
    "id": 1,
    "name": "Domino's",
    "address": "123 Pizza Lane"
  },
  {
    "id": 2,
    "name": "Pizza Inn",
    "address": "456 Cheese Street"
  }
]
GET /restaurants/1
Response:

json
Copy code
{
  "id": 1,
  "name": "Domino's",
  "address": "123 Pizza Lane",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Cheese, Sauce"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Cheese, Pepperoni"
    }
  ]
}
DELETE /restaurants/1
Response:

json
Copy code
{}
If restaurant has no associated restaurant_pizzas. If there are linked pizzas, deletion fails with an error message.

GET /pizzas
Response:

json
Copy code
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Cheese, Sauce"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Cheese, Pepperoni"
  }
]
POST /restaurant_pizzas
Request Body:

json
Copy code
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
Response:

json
Copy code
{
  "id": 1,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}

###### Validation Rules
price must be a number between 1 and 30 (inclusive)

pizza_id and restaurant_id must exist in their respective tables

On validation failure:

json
Copy code
{
  "errors": ["Validation failed: Price must be between 1 and 30"]
}

###### Postman Usage Instructions
Download the collection file (already provided or from GitHub):

challenge-1-pizzas.postman_collection.json

Import the file into Postman:

Open Postman

Click on Import → Upload Files

Select challenge-1-pizzas.postman_collection.json

Use the 5 provided requests:

Make sure your server is running: flask run

The base URL should be: http://127.0.0.1:5000

Run GET, POST, and DELETE requests as needed