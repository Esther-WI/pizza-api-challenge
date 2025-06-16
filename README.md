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

3 **Run the Flask application**
cd server
flask db init           # only once
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py          # seed the database with sample data
flask run


